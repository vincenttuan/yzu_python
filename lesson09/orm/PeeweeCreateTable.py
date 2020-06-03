# http://docs.peewee-orm.com/en/latest/peewee/quickstart.html

from peewee import *

from lesson09.orm.Entity import Person, Pet
import lesson09.orm.Entity as e

if __name__ == '__main__':
    e.getDB().connect()
    e.getDB().create_tables([Person, Pet])
    e.getDB().close()