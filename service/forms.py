from django import forms

from service.models import Mailing, Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        exclude = ('status', 'user',)


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('user',)
