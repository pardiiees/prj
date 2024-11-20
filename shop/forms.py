

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': ' نام و نام خانوادگی'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'placeholder': 'eg.example@email.com'}))
    text = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'placeholder': 'پیام خود را در این قسمت وارد کنید'}))
    def clean_sender_(self):
        s=self.cleaned_data["sender"]
        if len(s)<6:
            raise forms.ValidationError("نام و نام خانوادگی باید حداقل 6 کاراکتر باشد")
        return s