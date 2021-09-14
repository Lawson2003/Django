from django import forms
from .models import MyPost
class MyPostForm(forms.ModelForm):
	title=forms.CharField(label="Title",widget=forms.TextInput(attrs={
		'class':'form-control',
		}))
	content=forms.CharField(label="Details",widget=forms.Textarea(attrs={
		'class':"form-control",
		}))
	class Meta:
		model=MyPost
		fields="__all__"
