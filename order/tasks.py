from celery import shared_task
from django.core.mail import send_mail
from customer.models import Customer
from django.conf import settings


@shared_task
def order_create(customer_id, comment):
    customer = Customer.objects.get(id=customer_id)
    print(customer)
    subject = "Номер заказа {}".format(customer_id)
    message = """Здраствуйте {}, ваш заказ оформлен,  ваш id {}.""".format(
        customer.first_name, customer.id
    )
    mail_sent = send_mail(subject, message, settings.EMAIL_HOST_USER, [customer.email])
    my_sent = send_mail(
        "New order",
        f"""{customer.first_name} {customer.last_name},
                            сделал заказ id = {customer_id}, мобильный {customer.phone},
                            комментарий к заказу {comment}""",
        settings.EMAIL_HOST_USER,
        [settings.RECIPIENTS_EMAIL],
    )
    return mail_sent, my_sent
