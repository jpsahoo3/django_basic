from django import forms

class FeedbackForm(forms.Form):
    email = forms.CharField(label='Email', max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    title = forms.CharField(label='Title', max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label='Subject Desc', max_length=200, widget=forms.Textarea(attrs={'class':'form-control'}))