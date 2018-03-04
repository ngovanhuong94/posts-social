from django import forms 
from .models import Post

class PostCreateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text')
		widgets = {
			'title': forms.TextInput(attrs={"class": "form-control"}),
			"text": forms.Textarea(attrs={"class": "form-control editable medium-editor-textarea"})
		}

