from django.db import models
#  for user profile - video 16
from django.contrib.auth.models import User



# Create your models here.
class Activity(models.Model):
    # relationship- Many(Orders) have One(Customer) 
    # creating a reference of customer in an order
    # when customer deletes the order: set its customer value to null
    user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL) 

    # for dropdown menu
    ITEMS = (
            ('Take a Walk', 'Take a Walk'),
            ('Listen to Music', 'Listen to Music'),
            ('Read a Book', 'Read a Book'),
            ('Play a Game','Play a Game'),
            ('Chat with Friends', 'Chat with Friends'),
            ('Eat Healthy Food', 'Eat Healthy Food'),
            ('Meditate', 'Meditate'),
            ('Spend Time with Family', 'Spend Time with Family'),
            ('Feelings', 'Feelings'),
            ('Just Dance', 'Just Dance'),
            ('Do Yoga', 'Do Yoga'),
            ('Have 8hrs of Sleep', 'Have 8hrs of Sleep'),
            ('Go Shopping', 'Go Shopping'),
            ('Be a Painter', 'Be a Painter'),
            ('Write a Story', 'Write a Story'),
            ('Make a Todo List', 'Make a Todo List'),
            
            )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    activity = models.CharField(max_length=200, null=True, choices=ITEMS)
    # print(dir(activity))

    # to display customer name in html template
    def __str__(self):
        return self.activity

