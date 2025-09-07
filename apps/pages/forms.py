from django import forms

from apps.pages.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['is_read', 'comment']


    def clean(self):
        print("Object level validation")
        print(self.cleaned_data)
        return super().clean()