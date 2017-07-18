from aiomysql.sa import create_engine
import sqlalchemy as sa
from sanic import Sanic
from sanic.response import json
import json as jsonToStr

database_name = 'test'
database_host = '127.0.0.1'
database_user = 'root'
database_password = '123456'

metadata = sa.MetaData()
user = sa.Table('user', metadata,
                sa.Column('u_id', sa.Integer, primary_key=True),
                sa.Column('name', sa.String), sa.Column('password', sa.String))

app = Sanic(name=__name__)


@app.listener('before_server_start')
async def prepare_db(app, loop):
    db_config = {
        'user': database_user,
        'db': database_name,
        'host': database_host,
        'password': database_password
    }
    app.pool = {
        'sqlalchemy': await create_engine(**db_config)
    }


@app.listener('before_server_stop')
async def stop(app, loop):
    await app.pool['sqlalchemy'].close()


@app.route('/')
async def handler(request):
    async with app.pool['sqlalchemy'].acquire() as conn:
        result = []
        async for row in conn.execute(user.select()):
            result.append({
                'name': row.name,
                'password': row.password
            })
        return json({'user': result})


@app.route('/delete/<name:string>')
async def remove_user(request, name):
    print('name:', name)
    async with app.pool['sqlalchemy'].acquire() as conn:
        trans = await conn.begin()
        await conn.execute(user.insert().values(name="xxha", password="zzzz"))
        await conn.execute(user.insert().values(name="ddd", password="llll"))
        await conn.execute(user.update().where(user.c.name == "wang").
                           values(password="0000"))
        await trans.commit()

        result = []
        async for row in conn.execute(user.select()):
            result.append({
                'name': row.name,
                'password': row.password
            })

        print('current result:', jsonToStr.dumps(result))
        return json({'message': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888,  workers=4)
