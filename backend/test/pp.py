from pony.orm import (Database, Required, Optional, db_session, sql_debug,
                      commit, select, Set)
from pony.converting import str2datetime
import json
from datetime import datetime

db = Database()
db.bind(
    provider='mysql',
    host='127.0.0.1',
    user='root',
    passwd='123456',
    db='test')
sql_debug(True)


class Person(db.Entity):
    name = Required(str)
    age = Optional(int)
    order = Set(lambda: Order)
    date_create = Optional(datetime)


class Order(db.Entity):
    no = Required(str)
    content = Required(str)
    person = Optional(Person)


db.generate_mapping(create_tables=True)


def p2dic(person):
    return {'name': person.name, 'age': person.age}


with db_session:
    p = Person[1]
    order2 = Order(no='100232312121', content='tt', person=p)
    # p = Person(
    #     name='world',
    #     order=order1,
    #     date_create=str2datetime('2017-07-02 12:00:00'))
    persons = select(p for p in Person)
    for p in persons:
        print('person name:', p.name)
        print('person info:', json.dumps(p, default=p2dic))
