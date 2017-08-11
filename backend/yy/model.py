from pony.orm import (Database, Required, Optional, db_session, sql_debug)
from datetime import datetime

db = Database()
db.bind(
    provider='mysql',
    host='127.0.0.1',
    user='root',
    passwd='123456',
    db='test')

sql_debug(True)


class Film(db.Entity):
    cn_name = Required(str, 500)
    en_name = Optional(str, 500)
    cn_score = Optional(str, 10)
    en_score = Optional(str, 10)
    download_link = Required(str, 1000)
    date_create = Required(
        datetime, default=datetime.now(), sql_default='now()')
    date_update = Required(
        datetime, default=datetime.now(), sql_default='now()')


class Config(db.Entity):
    type = Required(str, 20)
    value = Required(str, 500)


class Category(db.Entity):
    content = Required(str, 20)
    alt_info = Optional(str, 200)
    date_create = Required(datetime)
    date_update = Required(datetime)


class Tag(db.Entity):
    content = Required(str, 20)
    date_create = Required(datetime)
    date_update = Required(datetime)


# create only at first time
db.generate_mapping(create_tables=True)
