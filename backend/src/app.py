from sanic import Sanic
from sanic.response import json
from aiomysql.sa import create_engine

from model.model import tag
import config.db_config as config

app = Sanic(name=__name__)


@app.listener('before_server_start')
async def prepare_db(app, loop):
    db_config = config.db_config
    app.pool = {'sqlalchemy': await create_engine(**db_config)}


@app.listener('before_server_stop')
async def stop(app, loop):
    print('===========> Something before after server ...')
    await app.pool['sqlalchemy'].close()


@app.route('/')
async def handler(request):
    async with app.pool['sqlalchemy'].acquire() as conn:
        result = []
        async for row in conn.execute(tag.select()):
            result.append({'content': row.content})
        return json({'content': result})


@app.route('/add')
async def remove_user(request):
    async with app.pool['sqlalchemy'].acquire() as conn:
        trans = await conn.begin()
        await conn.execute(tag.insert().values(
            content="xxha", date_create='2017-07-07 00:00:00'))
        await conn.execute(tag.insert().values(
            content="xxha", date_create='2017-07-07 00:00:00'))
        await conn.execute(
            tag.update().where(tag.c.id == 1).values(content="0000"))
        await trans.commit()

        return json({'message': 'ok'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, workers=4)
