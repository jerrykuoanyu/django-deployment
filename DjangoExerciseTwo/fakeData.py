import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DjangoExerciseTwo.settings')

import django
django.setup()


## Fake PIP SCRIPT

import random
from userInfo.models import User
from faker import Faker

fakegen = Faker()

def add_user():
    t = User.objects.get_or_create(first_name=fakegen.first_name(),last_name=fakegen.last_name(),email=fakegen.email())[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        #get the topic for the entry

        top = add_user()




if __name__ == '__main__':
    print("populating script!")
    populate(N=20)
    print("populating complete!")
