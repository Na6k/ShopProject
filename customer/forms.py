from .models import Customer
from django import forms



DELIVERY_1 = "B"  # Delivery tupe : BelPost
DELIVERY_2 = "E"  # Delivery tupe : EuroPost
DELIVERY_3 = "S"  # Delivery tupe : SDEC
DELIVERY_4 = "P"  # Delivery tupe : Pickup
DELIVERY_CHOISES = [
        (DELIVERY_1, "Белпочта"),
        (DELIVERY_2, "Европочта"),
        (DELIVERY_3, "СДЕК"),
        (DELIVERY_4, "Самовывоз"),
    ]


class CustomerCreatedForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={"type": "text", "placeholder": "Имя"},
        ),
    )

    last_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={"type": "text", "placeholder": "Фамилия"},
        ),
    )

    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={"type": "text", "placeholder": "Мобильный телефон"},
        ),
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={"type": "email", "placeholder": "Enter email address"},
        ),
    )

    country = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={"class": "wide", "type": "text", "placeholder": "Страна"},
        ),
    )

    city = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"type": "text", "placeholder": "Город"},
        ),
    )

    region = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={"type": "text", "placeholder": "Область"},
        ),
    )

    street = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"type": "text", "placeholder": "Улица"},
        ),
    )

    address = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"type": "text", "placeholder": "Дом(номер/корпус), Квартира(номер)"},
        ),
    )

    post_code = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"type": "text", "placeholder": "Индекс"},
        ),
    )

    comment_to_order = forms.CharField(
        max_length=1024,
        required=False,
        widget=forms.Textarea(
            attrs={
                "id": "checkout-mess",
                "cols": "30",
                "rows": "10",
                "placeholder": "Если хотите добавить комментарий, оставьте его сдесь",
                "default": "none",
            },
        ),
    )

    delivery_type = forms.ChoiceField(choices=DELIVERY_CHOISES, widget=forms.Select(attrs={'class':'wide'}))

    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "country",
            "city",
            "region",
            "street",
            "address",
            "post_code",
        ]
