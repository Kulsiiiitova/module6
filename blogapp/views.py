from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import BlogPost


class BlogPostsListView(ListView):
    model = BlogPost
    template_name = 'posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostsCreateView(CreateView):
    model = BlogPost
    template_name = 'posts_form.html'
    fields = ('name', 'content', 'picture', )
    success_url = reverse_lazy('blogapp:posts_list')


class BlogPostsDetailView(DetailView):
    model = BlogPost
    template_name = 'posts_details.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogPostsUpdateView(UpdateView):
    model = BlogPost
    template_name = 'posts_form.html'
    fields = ('name', 'content', 'picture', )

    def get_success_url(self):
        return reverse_lazy('blogapp:posts_details', args=[self.kwargs.get('pk')])


class BlogPostsDeleteView(DeleteView):
    model = BlogPost
    template_name = 'posts_confirm_delete.html'
    success_url = reverse_lazy('blogapp:posts_list')
    context_object_name = 'post'




