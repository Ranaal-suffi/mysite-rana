"""missing"""
from django.conf import settings # Import Django's Loaded settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
#from django.db.models import Count
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.query import QuerySet


# Create your models here.
class Topic(models.Model):
    """missing"""
    name = models.CharField(
        max_length=50,
        unique=True  # No duplicates!
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        """missing"""
        return self.name
    def get_absolute_url(self):
        """missing"""
        return reverse(
            'topic-detail',
            kwargs={
                'slug': self.slug
            })
    def get_posts(self):
        """Missing"""
        return self.blog_posts.all()

class PostQuerySet(models.QuerySet):
    """missing"""
    def published(self):
        """Missing"""
        return self.filter(status=self.model.PUBLISHED)

    def drafts(self):
        """missing"""
        return self.filter(status=self.model.DRAFT)

    def get_authors(self):
        """missing"""
        User = get_user_model()
        # Get the users who are authors of this queryset
        return User.objects.filter(blog_posts__in=self).distinct()

    #def get_topics(self):
        #return Topic.objects.all().annotate(num_posts=Count('blog_posts')).order_by('-num_posts')


class Post(models.Model):
    """
    Represents a blog post
    """
    DRAFT = 'draft'
    PUBLISHED ='published'
    STATUS_CHOICES =[
        (DRAFT, 'draft'),
        (PUBLISHED, 'published'),
    ]
    title = models.CharField(max_length=255)
    slug = models.SlugField(
        null=False,
        help_text= 'The date & time this article was published',
        unique_for_date='published', # Slug is unique for publication date
        blank = False,
    )
    banner = models.ImageField(
        blank=True,
        null=True,
        help_text='A banner image for the post'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, #The Django auth user model
        on_delete=models.PROTECT, # Prevent posts from being deleted
        related_name ='blog_posts', #This on the user model
        null= False,
        blank = False
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT,
        help_text='Set to "published" to make this post pblicly visible',
    )
    topics = models.ManyToManyField(
        Topic,
        related_name='blog_posts'
    )
    
    content = RichTextUploadingField()
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text ='The date & time this artiicle was published',
    )
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save
    objects = PostQuerySet.as_manager()

    def __str__(self):
        return str(self.title)
    def publish(self):
        """Publishes this post"""
        self.status = self.PUBLISHED
        self.published = timezone.now()  # The current datetime with timezone
    def get_absolute_url(self):
        """missing"""
        if self.published:
            kwargs = {
                'year': self.published.year,
                'month': self.published.month,
                'day': self.published.day,
                'slug': self.slug
            }
        else:
            kwargs = {'pk': self.pk}

        return reverse('post-detail', kwargs=kwargs)

class CommentQuerySet(models.QuerySet):
    """missing"""
    def published(self):
        """Missing"""
        return self.filter(status=self.model.PUBLISHED)

    def drafts(self):
        """missing"""
        return self.filter(status=self.model.DRAFT)

    def get_authors(self):
        """missing"""
        User = get_user_model()
        # Get the users who are authors of this queryset
        return User.objects.filter(blog_comments__in=self).distinct()

class Comment(models.Model):
    """Missing"""
    post= models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        null= True,
        blank = True
        )
    #approved = models.BooleanField(default = False)
    name= models.CharField( max_length= 10)
    email = models.EmailField()
    content = models.TextField(max_length=200)
    approved = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = CommentQuerySet.as_manager()
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text ='The date & time this comment was published',)

    def __str__(self):
        return f'{self.name} re: {self.post}'

    class Meta:
        ordering = ['-created']


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    submitted = models.DateTimeField(
        null=True,
        blank=True,
        help_text ='The date & time this artiicle was published',)
    #submitted = models.DateTimeField(auto_now_add=True)

    #class Meta:
        #ordering = ['-submitted']

    def __str__(self):
        return f'{self.submitted.date()}: {self.email}'
class PhotoContest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    banner = models.ImageField(
        blank=True,
        null=True,
        help_text='A banner image for the contest')
    submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.submitted.date()}: {self.email}'
class Meta:
    """Missing"""
    ordering = ['name','-created','-submitted']
