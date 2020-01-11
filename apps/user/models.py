from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, form_data):
        errors=[]
        
        if len(form_data['fname'])<2 or not(form_data['fname'].isalpha()):
            errors.append('First name must contain at least 2 letters and no numbers and special characters')
        
        if len(form_data['lname'])<2 or not(form_data['lname'].isalpha()):
            errors.append('Last name must contain at least 2 letters and no numbers and special characters')
        
        if len(form_data['pnum'])<15 or len(form_data['pnum'])>15 or not(form_data['pnum'].isdigit()):
            errors.append('Personal number must contain 15 numbers and no letters or special characters')

        if len(form_data['email']) < 1:
            errors.append("Email cannot be blank!")
        elif not EMAIL_REGEX.match(form_data['email']):
            errors.append("Invalid Email Address!")
        
        if len(form_data['password']) < 8:
            errors.append('Password must be more than 8 characters!')
        elif form_data['password'] != form_data['confpassword']:
            errors.append('Password and password confirmation must be the same!')

        existing_emails=User.objects.filter(email=form_data['email'])
        if existing_emails:
            errors.append('Email already used!')
        
        existing_pnum = User.objects.filter(personal_number = form_data['pnum'])
        if existing_pnum:
            errors.append('Personal number already used!')
        
        return errors
    
    def basic_validator(self, form_data):
        errors = []
        if len(form_data['password']) < 8:
            errors.append('Password must be more than 8 characters!')
        elif form_data['password'] != form_data['confpassword']:
            errors.append('Password and password confirmation must be the same!')

        return errors   

    def create_user(self, form_data):
        pw_hash = bcrypt.hashpw(form_data['password'].encode('utf-8'), bcrypt.gensalt()) 
        user = User.objects.create(
            first_name = form_data['fname'], 
            last_name = form_data['lname'], 
            personal_number = form_data['pnum'],
            email = form_data['email'], 
            pw_hash = pw_hash.decode('utf-8')
        )
        return user.id
    
    def login(self, form_data):
        existing_user= User.objects.filter(email = form_data['email'])
        if existing_user:
            user = existing_user[0]
            if bcrypt.checkpw(form_data['password'].encode('utf-8'), user.pw_hash.encode('utf-8')):
                return (True, user.id)
        return(False, 'Email or password incorrect')
    
    def change_password(self, form_data, user_id):
        pw_hash = bcrypt.hashpw(form_data.encode('utf-8'), bcrypt.gensalt())
        user = User.objects.get(id=user_id)
        user.pw_hash = pw_hash.decode('utf-8')
        user.save()


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    personal_number = models.IntegerField()
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=255, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = UserManager()

    def __repr__(self):
        return "User({}, {})".format(self.first_name, self.last_name) 



