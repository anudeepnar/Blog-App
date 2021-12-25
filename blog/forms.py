from django import forms
from blog.models import Blog, Comment, Reply, Lead


class BlogCreateForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'description', 'image']

class LeadCreateForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = ['title', 'description', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        labels = {"body":"Comment:"}

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':70, 'placeholder':"Enter Your Comment"}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body',)

        widgets = {
            'reply_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10}),
        }