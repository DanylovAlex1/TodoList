from rest_framework import serializers

from .models import Board, TodoList


class BoardListAPIViewSerializer(serializers.Serializer):
    title = serializers.CharField()
    count = serializers.IntegerField()


class BoardCreateAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields='__all__'
        # fields = ['title', ]


class TodoListAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'
        #fields = ['title', 'done']
