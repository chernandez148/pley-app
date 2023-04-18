from app import app
from models import db, User

with app.app_context():

    print('Deleting existing users...')
    User.query.delete()

    print('Creating bird objects...')
    user1 = User(fname='Chickadee', lname='Poecile Atricapillus', email='email1@email.com')
    user2 = User(fname='Grackle', lname='Quiscalus Quiscula', email='email2@email.com')
    user3 = User(fname='Starling', lname='Sturnus Vulgaris', email='email3@email.com')
    user4 = User(fname='Dove', lname='Zenaida Macroura', email='email4@email.com')

    print('Adding user objects to transaction...')
    db.session.add_all([user1, user2, user3, user4])

    print('Committing transaction...')
    db.session.commit()

    print('Complete.')