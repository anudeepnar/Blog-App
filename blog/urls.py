from django.urls import path
from blog.views import home, BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, LeadCreateView, LeadUpdateView, LeadDeleteView


app_name = "blog"

urlpatterns = [
    path('', home, name='home'),
    path('blog/', BlogListView.as_view(), name='blog_list_view'),
    path('blog/lead', LeadCreateView.as_view(), name='lead_create_view'),
    path('blog/<slug:slug>/update', LeadUpdateView.as_view(), name='lead_update_view'),
    path('blog/<slug:slug>/delete', LeadDeleteView.as_view(), name='lead_delete_view'),
    path('blog/post/create/', BlogCreateView.as_view(), name='blog_create_view'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail_view'),
    path('blog/<slug:slug>/update/', BlogUpdateView.as_view(), name='blog_update_view'),
    path('blog/<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete_view'),
]