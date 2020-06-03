from datetime import date

from peewee import *

from lesson09.orm.Entity import Person, Pet

for person in Person.select():
    print(person.name, person.birthday)

print("----------------------")

for person in Person.select():
    print(person)
    for pet in person.pets:
        print("   ", pet)

print("----------------------")
for pet in Pet.select():
    print(pet.name, pet.animal_type, pet.owner.name)
