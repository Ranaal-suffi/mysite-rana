"""missing"""
from django.contrib import admin
from . import models
class CommentInlineAdmin(admin.StackedInline):
    """missing"""
    model= models.Comment
class PostAdmin(admin.ModelAdmin):
    """missing"""
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
    """missing"""
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    """missing"""
    list_display =(
        "name",
        "email",
        "content",
        "post"
    )

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'last_name',
        'first_name',
        'submitted'
    )
    # Make these fields read-only in the admin
    readonly_fields = (
        'first_name',
        'last_name',
        'email',
        'message',
        'submitted'
    )
@admin.register(models.PhotoContest)
class PhotoContestAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'last_name',
        'first_name',
        'submitted',
    )
    
    
     