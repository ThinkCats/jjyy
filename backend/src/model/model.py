from sqlalchemy import (MetaData, Column, Table, String, DateTime, BigInteger)

metadata = MetaData()

film = Table('film', metadata,
             Column('id', BigInteger, primary_key=True, autoincrement=True),
             Column('cn_name', String(500)),
             Column('en_name', String(500)),
             Column('cn_score', String(10)),
             Column('en_score', String(10)),
             Column('download_link', String(1000)),
             Column('date_create', DateTime), Column('date_update', DateTime))

category = Table('category', metadata,
                 Column(
                     'id', BigInteger, primary_key=True, autoincrement=True),
                 Column('film_id', BigInteger),
                 Column('content', String(20)),
                 Column('alt_info', String(200)),
                 Column('date_create', DateTime),
                 Column('date_update', DateTime))

tag = Table('tag', metadata,
            Column('id', BigInteger, primary_key=True, autoincrement=True),
            Column('film_id', BigInteger),
            Column('content', String(20)),
            Column('date_create', DateTime), Column('date_update', DateTime))

hello = 'hello world'
