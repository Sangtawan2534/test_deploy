from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    nickname = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(blank=True, null=True)
    body = models.TextField(null=True, blank=True)
    author_pic = models.ImageField(upload_to="featured-images/", null=True, blank=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=40)
    courses = models.CharField(max_length=40)
    detail = models.TextField(null=True, blank=True)
    subject_pic = models.ImageField(upload_to="featured-images/", null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    review_name = models.CharField(max_length=40)
    review_body = models.TextField(null=True, blank=True)
    review_pic = models.ImageField(upload_to="featured-images/", null=True, blank=True)

    def __str__(self):
        return self.review_name

class Post(models.Model):  # สร้างClassชื่อPost
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)  # สร้าง
    description = models.CharField(max_length=120, blank=True, null=True)
    body = models.TextField()  # bodyคือชื่อคอลัมประเภทตัวอักษรคือTextfield
    date_created = models.DateTimeField(auto_now_add=True)  # auto_now_addคือสร้างครั้งเดียวไม่เปลี่ยนแล้ว
    date_updated = models.DateTimeField(auto_now=True)  # auto_nowคือมีการเปลี่ยนข้อมูลให้เรื่อยๆ
    featured_pic = models.ImageField(upload_to="featured-images/", blank=True, null=True)  # รูปภาพ
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

class Contact(models.Model):
    subject = models.CharField(max_length=120)
    sender = models.CharField(max_length=80)
    email = models.EmailField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.subject