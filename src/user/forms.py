from user.models import Contact, User
from user.tasks import send_mail_async

from django import forms


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email',
                  'first_name',
                  'last_name',
                  'age',
                  'phone'
                  )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = user.email.lower()
        user.first_name = user.first_name.title()
        user.last_name = user.last_name.title()
        user.save()
        return user


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('subject',
                  'text',
                  )

    def save(self):
        subject = self.cleaned_data['subject']
        text = self.cleaned_data['text']
        send_mail_async.delay(subject, text)
