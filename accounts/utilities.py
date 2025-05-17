import secrets
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_verification_email(user_email, verification_code):
    subject = 'Verify Your Email Address'
    html_message = render_to_string('accounts/verification_email.html', {
        'verification_code': verification_code,
    })
    plain_message = strip_tags(html_message)
    from_email = 'eduraeducation25@gmail.com'
    to_email = [user_email]

    send_mail(subject, plain_message, from_email, to_email, html_message=html_message)

def password_reset_email(user_email, verification_code):
    subject = 'Password Reset Request'
    html_message = render_to_string('accounts\password_reset_email.html', {
        'verification_code': verification_code,
    })
    plain_message = strip_tags(html_message)
    from_email = 'eduraeducation25@gmail.com'
    to_email = [user_email]

    send_mail(subject, plain_message, from_email, to_email, html_message=html_message)

def generate_verification_code():
    return secrets.token_hex(4)  # Generates an 8-character hex code