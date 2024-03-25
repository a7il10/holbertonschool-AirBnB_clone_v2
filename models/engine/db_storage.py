#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = 'HBNB_MYSQL_USER'
        pwd = 'HBNB_MYSQL_PWD'
        host = 'HBNB_MYSQL_HOST'
        db = 'HBNB_MYSQL_DB'
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        classes = ['State', 'City', 'User', 'Place', 'Review']
        objs = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            for obj in self.__session.query(cls):
                objs[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for c in classes:
                for obj in self.__session.query(eval(c)):
                    objs[obj.__class__.__name__ + '.' + obj.id] = obj
        return objs
    
    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        self.__session.remove()