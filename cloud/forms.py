from django import forms


class PubCloudForms(forms.Form):
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    email = forms.EmailField(min_length=2, max_length=50)
    phone_number = forms.RegexField(
        regex=r'^(?:\+971|00971|0)?(?:50|51|52|55|56|2|3|4|6|7|9)\d{7}$',
        error_messages={'invalid': 'Phone number must be UAE format. For example: +971563718710'}
    )
    subject = forms.CharField(max_length=255, min_length=2)
    message = forms.CharField(widget=forms.Textarea())
    is_agree = forms.BooleanField(required=True)
