from django.contrib import admin
from blog.models import Blog, Lead, Testimonial, Comment, Reply
# Register your models here.

class AdminBlog(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',) }

class AdminLead(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title',) }


admin.site.register(Blog, AdminBlog)
admin.site.register(Lead, AdminLead)
admin.site.register(Testimonial)
admin.site.register(Comment)
admin.site.register(Reply)