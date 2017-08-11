from sanic import Sanic
from sanic.response import json

from model.model import tag
import config.db_config as config

app = Sanic(name=__name__)


@app.route('/')
async def handler(request):
        return json({'content': 'hello'})


@app.route('/add')
async def remove_user(request):
        return json({'message': 'ok'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, workers=4)
