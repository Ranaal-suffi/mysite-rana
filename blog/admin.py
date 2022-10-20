from django.contrib import admin
from . import models

class CommentInlineAdmin(admin.StackedInline):
    model= models.Comment
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'status',
        'created',
        'updated',
    ]
    list_filter = [
        'status', 'topics'
    ]
    prepopulated_fields = {'slug': ('title',)}
    search_fields = [
        'title',
        'author__username',
        'author__first_name',
        'author__last_name'
    ]
    inlines= [CommentInlineAdmin]

# Register the `Post` model
admin.site.register(models.Post, PostAdmin)

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display =(
        "name",
        "email",
        "content",
        "post"
    )   
    