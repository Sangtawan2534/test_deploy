from django.shortcuts import render
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from . models import Post, Review, Author, Subject
from django.db.models import Q #ทำตัวค้นหา

# Create your views here.
def home(request):
    all_posts = Post.objects.all()
    all_review = Review.objects.all()
    all_author = Author.objects.all()
    all_subject = Subject.objects.all()

    form = ContactForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        # print("Okey, this is POST")
    else:
        form = ContactForm()
        # print("Not Okey")


    return render(request, 'blog/home.html', {'all_posts': all_posts, 'all_review': all_review, 'all_author': all_author, 'all_subject': all_subject, 'form': form})



def contact(request):
    form = ContactForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        #print("Okey, this is POST")
    else:
        form = ContactForm()
        #print("Not Okey")
    return render(request, 'blog/forms.html', {'form': form})


def blog_detail(request, slug):

    #Query only post
    single_post = Post.objects.get(slug=slug)
    all_post = Post.objects.all()
    all_subject = Subject.objects.all()

    return render(request, 'blog/blog-detail.html', {'single_post': single_post, 'all_post': all_post, 'all_subject': all_subject})

def search(request):
    search_post = request.GET.get('search')#searchนี้มาจากตรงbase.htmlที่เราสร้างตรงform

    if search_post:
        #print("Okay")
        #print(search_post)
        post = Post.objects.filter( Q(title__icontains=search_post) )
    else:
        pass

    return render(request, 'blog/search.html', {'post': post, 'search_post': search_post})
