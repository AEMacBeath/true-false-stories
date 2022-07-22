from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Story, Comment, Headline


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


@admin.register(Headline)
class HeadlineAdmin(admin.ModelAdmin):

    list_display = ('title', 'displayed', 'created')
    actions = ['display_headline']

    def display_headline(self, request, queryset):
        queryset.update(displayed=True)
