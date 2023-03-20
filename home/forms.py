from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "name": "name",
                "placeholder": "Фамилия Имя",
            },
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "type": "email",
                "name": "email",
                "placeholder": "Email",
            },
        ),
    )
    subject = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "name": "subject",
                "placeholder": "Тема",
            },
        ),
    )
    company = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "text",
                "name": "website",
                "placeholder": "Компания",
            },
        ),
    )
    message = forms.CharField(
        max_length=1024,
        widget=forms.Textarea(
            attrs={
                "name": "message",
                "class": "form-control",
                "placeholder": "Напишите свое сообщение",
            },
        ),
    )
