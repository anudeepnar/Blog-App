from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from PIL import Image
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=2000, blank=True)
    image = models.ImageField(upload_to = 'blog_posts/', blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    #featured = models.BooleanField(default=False) for featured posts

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
        # img = Image.open(self.image.path)

        # if img.height > 250 or img.width >200:
        #     output_size =(200, 250)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('blog:blog_detail_view', kwargs={'slug': self.slug})


    class Meta:
        ordering = ['created_at']

class Lead(models.Model):
    image = models.ImageField(default='', upload_to='lead/', blank=True)
    title = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # def get_absolute_url(self, *args, **kwargs):
    #     return reverse("blog:home")
    

class Testimonial(models.Model):
    name = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=500, blank= True)
    image = models.ImageField(default='',  upload_to='testimonial/', blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    blog_title = models.ForeignKey(Blog,null=True, on_delete=models.CASCADE,related_name='blogs')
    comm_name = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.comm_name = slugify("comment by" + "-" + str(self.author))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comm_name

    class Meta:
        ordering = ['-date_added']

class Reply(models.Model):
    comment_name = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='replies')
    reply_body = models.TextField(max_length=500)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reply to " + str(self.comment_name.comm_name)
