# pip install peewee
# http://docs.peewee-orm.com/en/latest/peewee/quickstart.html

from peewee import *

def getDB():
    return SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = getDB() # This model uses the "people.db" database.

    def __str__(self):
        return self.name + ", " + str(self.birthday)


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = getDB() # this model uses the "people.db" database

    def __str__(self):
        return self.name + ", " + self.animal_type
