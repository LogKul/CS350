from rest_framework import serializers
from tasks.models import *

'''
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id',
                  'task_name',
                  'description',
                  'completed',
                  'due_date')
'''


class AuthorSerializer(serializers.ModelSerializer):

    # id = serializers.CharField()

    class Meta:
        model = Author
        fields = ('id',
                  'name',)


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id',
                  'name',
                  'author',)
