from django import forms

class ContactForm(forms.Form):
	name=forms.CharField(max_length=40)
	subject = forms.CharField(max_length=100)
	email = forms.EmailField(required=False)#,label='Your e-mail address')
	message = forms.CharField(widget=forms.Textarea)#,label='Please type message here.')

