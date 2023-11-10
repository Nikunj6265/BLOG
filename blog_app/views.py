from django.shortcuts import render
from django.contrib import messages
from blog_app import forms
from django.views import View
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def home(request):
    my_object =  BlogPost.objects.all()
    object_size = len(my_object)
    return render(request, 'blog_app/home.html', {'my_object': my_object ,'object_size': object_size})

class detail(View):
    def get(self, request, pk):
        blog = BlogPost.objects.get(pk=pk)
        return render(request, 'blog_app/blogdetail.html',{'blog':blog})



@login_required()
def Myblogs(request):
    user = request.user
    my_object = BlogPost.objects.filter(author=user)
    object_size = len(my_object)
    return render(request, 'blog_app/myblog.html', {'my_object': my_object ,'object_size': object_size})

class register(View):
    def get(self, request):
        form = forms.RegistrationForm()
        return render(request, 'blog_app/register.html', {'form': form})

    def post(self, request):
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            form.save()
        return render(request, 'blog_app/register.html', {'form': form})



@method_decorator(login_required, name='dispatch')
class PostBlog(View):
    def get(self, request):
        form = forms.BlogPostform()
        return render(request, 'blog_app/upload.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        form = forms.BlogPostform(request.POST)
        if form.is_valid():
            usr = request.user
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            reg = BlogPost(author=usr,title=title, content=content)
            reg.save()
            messages.success(request, 'Congratulations!! Profile Updated Successfully')
           
            
        return render(request, 'blog_app/upload.html', {'form': form, 'active': 'btn-primary'})

