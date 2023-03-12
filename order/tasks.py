from celery import shared_task
from django.core.mail import send_mail
from customer.models import Customer
from django.conf import settings

@shared_task
def order_create(customer_id):
    customer = Customer.objects.get(id = customer_id)
    print(customer)
    subject = "Номер заказа {}".format(customer_id)
    message = '''Здраствуйте {}, ваш заказ оформлен,  ваш id {}.'''.format(customer.first_name, customer.id)
    mail_sent = send_mail(subject,
                          message,
                          'lanabau.python.dev@gmail.com',
                          [customer.email])
    return mail_sent

