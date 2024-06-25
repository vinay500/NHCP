from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings as SETTINGS
from .generate_verify_mail_token import generate_encrypted_token
import logging


# log configuration
logging.basicConfig(
    format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='[%d/%b/%Y %H:%M:%S]')
# examples

def send_registration_mail(recipient_email, recipient_name):
    
    email_token = generate_encrypted_token(recipient_email)
    logging.info(F"email_token in send_registration_mail:{email_token}")

    # Render the email template
    email_content = render_to_string('authentication/user_registration_mail.html', 
                                        {
                                            'recipient_name': recipient_name,
                                            'recipient_email': recipient_email,
                                            'email_token': email_token,
                                            'IP_ADDRESS': SETTINGS.IP_ADDRESS,
                                            'PORT': SETTINGS.PORT,
                                        }
                                    )
    # Send the email
    try:
        send_mail_status = send_mail(
            'Welcome to Swasth Medical Associates',
            email_content,
            SETTINGS.EMAIL_HOST_USER,  # Sender's email address
            [recipient_email],      # Recipient's email address
            # fail_silently=False,
            html_message=email_content,
        )
        logging.info(f"send_mail_status : {send_mail_status}")
        logging.info("User Registration Mail Sent Successfully")
        return True
    except Exception as e:
        logging.error('Exception: ',e)
        logging.error("Email Sending Failed, Error in send_registration_mail() :{email_token}")
        # return HttpResponse('Email sent successfully!')
        return False