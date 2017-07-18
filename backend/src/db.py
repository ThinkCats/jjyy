import aiomysql
from sanic import Sanic
from sanic.response import json

database_name = "test"
database_host = "127.0.0.1"
database_user = "root"
database_password = "123456"
app = Sanic()


@app.listener("before_server_start")
async def get_pool(app, loop):
    app.pool = {
        "aiomysql": await aiomysql.create_pool(host=database_host,
                                               user=database_user,
                                               password=database_password,
                                               db=database_name,
                                               maxsize=5)}
    async with app.pool['aiomysql'].acquire() as conn:
        async with conn.cursor() as cur:
            print("-------------------- >")
            await cur.execute('DROP TABLE IF EXISTS sanic_polls')
            print("<-------------------- >")
            await cur.execute("""CREATE TABLE sanic_polls (
                                    id serial primary key,
                                    question varchar(50),
                                    pub_date timestamp
                                );""")
            for i in range(0, 100):
                insert_sql = ("""INSERT INTO sanic_polls
                                (id, question, pub_date) VALUES ({}, {}, now())
                """.format(i, i)
                )
                print("=======================>: ",insert_sql)
                await cur.execute(insert_sql)


@app.route("/")
async def test():
    result = []
    data = {}
    async with app.pool['aiomysql'].acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT question, pub_date FROM sanic_polls")
            async for row in cur:
                result.append({"question": row[0], "pub_date": row[1]})
    if result or len(result) > 0:
        data['data'] = result
    return json(data)


if __name__ == '__main__':
    app.run(host="127.0.0.1", workers=4, port=12000)
