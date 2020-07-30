from django.contrib import admin
from .models import Board,TodoList


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title',)


@admin.register(TodoList)
class TodoAdmin(admin.ModelAdmin):
    search_fields = ['title','created']
    list_display = ('title','done')
    list_filter = ('done','user')

