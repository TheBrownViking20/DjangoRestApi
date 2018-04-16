from django.db import models

class Card(models.Model):
    CLASS_CHOICES= (
        ('mage','Mage'),
        ('warrior','Warrior'),
        ('assassin','Assassin'),
        ('druid','Druid'),
    )
    name = models.CharField(max_length=30)
    health = models.IntegerField()
    attack = models.IntegerField()
    ability = models.CharField(max_length=100)
    card_class = models.CharField(max_length=10,choices=CLASS_CHOICES,default='warrior')

    def __str__(self):
        return self.name
