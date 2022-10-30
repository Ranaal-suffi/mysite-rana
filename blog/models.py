from django.conf import settings # Import Django's Loaded settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models import Count


# Create your models here.
class Topic(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True  # No duplicates!
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=self.model.PUBLISHED)

    def drafts(self):
        return self.filter(status=self.model.DRAFT)

    def get_authors(self):
        User = get_user_model()
        # Get the users who are authors of this queryset
        return User.objects.filter(blog_posts__in=self).distinct()

    def get_topics(self):
        return Topic.objects.all().annotate(num_posts=Count('blog_posts')).order_by('-num_posts')


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
    content = models.TextField()
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text ='The date & time this artiicle was published',
    )
    created = models.DateTimeField(auto_now_add=True)  # Sets on create
    updated = models.DateTimeField(auto_now=True)  # Updates on each save

    objects = PostQuerySet.as_manager()

    #comment=models.ForeignKey(
        #Comment,
        #on_delete=models.PROTECT,
        #related_name='blog_posts',
        #null= False,
        #blank = False
    #)
    
    def __str__(self):
       return str(self.title)
    
    def publish(self):
        """Publishes this post"""
        self.status = self.PUBLISHED
        self.published = timezone.now()  # The current datetime with timezone

class Comment(models.Model):
    post= models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        null= True,
        blank = True
        )
    approved = models.BooleanField(
        default = False
    )
    name= models.CharField( max_length= 10)
    email = models.EmailField()
    content = models.TextField(max_length=200)
    published = models.DateTimeField(
        null=True,
        blank=True,
        help_text ='The date & time this comment was published',)
    #created = models.DateTimeField(auto_now_add=True)  # Sets on create
    #updated = models.DateTimeField(auto_now=True)  # Updates on each save
    #class Meta:
        #ordering = ['created_on']
    def __str__(self):
        return str(self.content)

class Meta:
    ordering = ['name','-created']










