from django.db import models
import uuid

class Token(models.Model):
    member_id = models.CharField(max_length=10)
    uid = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.member_id}'

def create_token(member_dict):
    token = Token.objects.create(
        member_id=member_dict['member_id'],
	uid=uuid.uuid1()
    )
    return token

def create_tokens(member_dicts):
    # Awkward muddling of db state change and list creation.
    return [{'member_id': member_dict['member_id'],
             'main_contact': member_dict['main_contact'],
             'phone': member_dict['phone'],
	         'uid': create_token(member_dict).uid}
	         for member_dict in member_dicts]