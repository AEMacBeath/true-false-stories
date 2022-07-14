from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Story, Comment


@admin.register(Story)
class StoryAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'updated', 'author')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'approved', 'created')
    list_filter = ('name', 'approved', 'created')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)
