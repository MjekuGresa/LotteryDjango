from __future__ import unicode_literals
from django.db import models
from ..user.models import User
from django.core.validators import validate_comma_separated_integer_list

class TicketManager(models.Manager):
    def create_ticket(self, form_data, user_id):
        user = User.objects.get(id = user_id)
        Ticket.objects.create(
            numbers_selected = form_data,
            creator = user
        )
    
class Ticket(models.Model):
    numbers_selected = models.CharField(validators=[validate_comma_separated_integer_list],max_length=200,blank=True,null=True,default='')
    creator = models.ForeignKey(User, related_name='tickets', on_delete = models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = TicketManager()

    def __repr__(self):
        return "Ticket({},{})".format(self.numbers_selected,self.creator) 



