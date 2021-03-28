from django.contrib import admin
from .models import Author, Post, Subject, Review, Contact
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')
    list_display = ('title', 'date_created', 'date_updated', 'author')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post,PostAdmin)

# Register your models here.
admin.site.register(Contact)
admin.site.register(Author)
admin.site.register(Subject)
admin.site.register(Review)
