from django.db import models

# Create your models here.
class AppUser(models.Model):
    full_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=200)

class todo(models.Model):
    choices_status = [
    ('C', 'completed'),
    ('P', 'pending'),
    ]
    
    priority_choices = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ]
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=choices_status)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    priority = models.CharField(max_length=6, choices=priority_choices)


    