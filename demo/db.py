from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

user_name = "root"
user_pwd = "1234"
db_host = "172.16.153.231"
db_name = "TEST"

DB_URL = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    user_pwd,
    db_host,
    db_name
)

engine = create_engine(DB_URL)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()