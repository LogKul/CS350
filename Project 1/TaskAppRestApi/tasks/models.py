from django.db import models
# from djongo import models

# Create your models here.

'''
class Task(models.Model):
    task_name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    completed = models.BooleanField(default=False)
    due_date = models.DateField()
    author_key = models.ForeignKey(User, on_delete=model.CASCADE)


class User(models.Model):
    user_name = models.CharField(max_length=70, blank=False)
    password = models.CharField(max_length=70, blank=False)
    first_name = models.CharField(max_length=70, blank=False)
    last_name = models.CharField(max_length=70, blank=False)
    team = models.CharField(max_length=70, blank=False)
    email = models.EmailField()
    team = models.ForeignKey(Team)
    points = models.IntegerField()


class Team(models.Model):
    team_name = models.CharField(max_length=70, blank=False, default='')
    total_points = models.IntegerField()


class LeaderboardEntry(models.Model):
    team = models.ForeignKey(Team)

id = models.AutoField(auto_created=True, unique=True,
                      primary_key=True, serialize=False)
'''


class Author(models.Model):
    name = models.CharField(max_length=70, blank=False)


class Book(models.Model):
    name = models.CharField(max_length=70, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
