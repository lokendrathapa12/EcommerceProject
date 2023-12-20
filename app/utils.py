# utils.py

from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import OrderedPlaced
from django.contrib.auth.models import User
from django.conf import settings

def send_sold_out_email(order_id):
    # Retrieve order information from the database
    order = OrderedPlaced.objects.get(id=order_id)
    product = order.product
    product_image = order.product.product_image_frontside
    product_owner_email = order.owner_email

    # Render email content using a template
    email_content = render_to_string('app/email_template.html', {'order': order, 'product': product,'product_image':product_image})

    # Send the email
    send_mail(
        'Subject: Product Sold Out',
        email_content,
        'settings.EMAIL_HOST_USER',  # Sender's email address
        [product_owner_email], # Product owner's email address
        fail_silently=False,
    )

def send_out_email_customer(order_id):
    order = OrderedPlaced.objects.get(id=order_id)
    product = order.product
    cus_email = order.email

    email_content = render_to_string('app/customer_email.html',{'order':order,'product':product,'cus_email':cus_email})

    send_mail(
        'subject: Your Order Placed',
        email_content,
        'settings.EMAIL_HOST_USER',
        [cus_email],
        fail_silently=False,
    )

def send_email_registration(user_id):
    user = User.objects.get(id = user_id)
    username = user.username
    email = user.email

    email_content = render_to_string('app/user_email.html',{'user':user,'username':username,'email':email})

    send_mail(
        'subject: Your Account create Successfully!!!',
        email_content,
        'settings.EMAIL_HOST_USER',
        [email],
        fail_silently=False
    )