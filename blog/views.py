from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView , DetailView, UpdateView, DeleteView, CreateView, FormView
#from django.views.generic.edit import CreateView
from blog.models import Blog, Lead, Testimonial
from blog.forms import BlogCreateForm, CommentForm, ReplyForm, LeadCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    latest_blogs = Blog.objects.order_by('-created_at')[:4]
    Context = {
        'leads' : Lead.objects.all(),
        'blogs' : Blog.objects.all(),
        'testimonials' : Testimonial.objects.all(),
        'latest_blogs':latest_blogs
    }
    return render(request, 'blog/home.html', Context)

class BlogListView(ListView):
    Model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/blog_list_view.html'  
    paginate_by = 2

    def get_queryset(self) :
        return Blog.objects.all() 


class BlogDetailView(DetailView, FormView):
    Model = Blog
    context_object_name = 'blog_detail'
    template_name = 'blog/blog_detail_view.html'
    form_class = CommentForm
    second_form_class = ReplyForm
    

    def get_queryset(self):
        return Blog.objects.all()


    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        if 'form' not in context:
            # request=self.request
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        # context['comments'] = Comment.objects.filter(id=self.object.id)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'form' in request.POST:
            # form_class = self.get_form_class()
            form_class = self.form_class
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)
        # print("the form name is : ", form)
        # print("form name: ", form_name)
        # print("form_class:",form_class)

        if form_name=='form' and form.is_valid():
            print("comment form is returned")
            return self.form_valid(form)
        elif form_name=='form2' and form.is_valid():
            print("reply form is returned")
            return self.form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail_view',kwargs={'slug':self.object.slug})
    

class BlogCreateView(LoginRequiredMixin, CreateView):
    form_class = BlogCreateForm
    Model = Blog
    #context_object_name = 'blogs'
    template_name = 'blog/blog_create_view.html'

    # def get_queryset(self):
    #     return Blog.objects.all()

    def get_success_url(self):
        return reverse_lazy('blog:blog_list_view')
    
    def form_valid(self, form, *args, **kwargs):
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    fields = ('title', 'description', 'image')
    Model = Blog
    context_object_name = 'blog_update'
    template_name = 'blog/blog_update_view.html'

    def get_queryset(self):
        return Blog.objects.all()

        #user can't update other posts
    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    Model = Blog
    success_url ='/'
    template_name = 'blog/blog_delete_view.html'

    def get_queryset(self):
        return Blog.objects.all()

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False

class LeadCreateView(CreateView):
    form_class = LeadCreateForm
    Model = Lead
    template_name = 'blog/lead_create_view.html'

    def get_success_url(self):
        return reverse_lazy('blog:home')
    
    def form_valid(self, form, *args, **kwargs):
        fm = form.save(commit=False)
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

class LeadUpdateView(UpdateView):
    fields = ('title', 'description', 'image')
    Model = Lead
    context_object_name = 'lead_update'
    template_name = 'blog/lead_update_view.html'

    def get_queryset(self):
        return Lead.objects.all()

    def get_success_url(self):
        return reverse_lazy('blog:home')

class LeadDeleteView(DeleteView):
    Model = Lead
    success_url ='/'
    template_name = 'blog/lead_delete_view.html'

    def get_queryset(self):
        return Lead.objects.all()




 
      