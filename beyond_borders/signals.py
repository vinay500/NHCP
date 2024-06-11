from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BeyondBordersDependents
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings as SETTINGS
import logging

logging.basicConfig(
    format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='[%d/%b/%Y %H:%M:%S]'
    )



@receiver(post_save, sender=BeyondBordersDependents) 
def notify_admin(sender, instance, created, **kwargs):
    logging.info("Sending mail to NHCP Admin")
    print("link: ",'http://{SETTINGS.IP_ADDRESS}:{SETTINGS.PORT}/view_dependents')
    if created:
        logging.info(F"sending mail to NHCP Admin")
        email_content = render_to_string('email_templates/nhcp_lead_notify.html',
                                            {
                                                'mail_heading': 'New Dependent Added',
                                                'mail_msg': 'New Dependent has been Added',
                                                'recipient_name': 'NHCP Admin',
                                                'recipient_email': SETTINGS.NHCP_ADMIN_MAIL,
                                                'booking_details_first_name': instance.first_name,
                                                'booking_details_mail': instance.email,
                                                'ref_link':f'http://{SETTINGS.IP_ADDRESS}:{SETTINGS.PORT}/view_dependents',
                                                'model':'beyond_borders'
                                            }
                                        )
        # Send the email
        try:
            send_mail_status = send_mail(
                'New Dependent Added',
                email_content,
                SETTINGS.EMAIL_HOST_USER,  # Sender's email address
                ['vinaymadugula20@gmail.com',],      # Recipient's email address
                # fail_silently=False,
                html_message=email_content,
            )
            logging.info(f"send_mail_status : {send_mail_status}")
            logging.info("Mail Sent Successfully to NHCP Admin")
            return True
        except Exception as e:
            print('e: ',e)
            logging.error("Email Sending Failed, Error in send_registration_mail() :{email_token}")
            return False