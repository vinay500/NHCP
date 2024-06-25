from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ServiceRegistrations
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings as SETTINGS
import logging

logging.basicConfig(
    format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='[%d/%b/%Y %H:%M:%S]')



@receiver(post_save, sender=ServiceRegistrations) 
def notify_admin(sender, instance, created, **kwargs):
    logging.info("in notify_admin")
    print("in notify_admin")
    print("instance.name: ",instance.name)
    print("link: ",'http://{SETTINGS.IP_ADDRESS}:{SETTINGS.PORT}/booked_services')
    if created:
        logging.info(F"sending mail to NHCP Admin")
        email_content = render_to_string('email_templates/nhcp_lead_notify.html',
                                            {
                                                'mail_heading': 'New Home Care Service Booking',
                                                'mail_msg': 'You have received a new home care service booking',
                                                'recipient_name': 'NHCP Admin',
                                                'recipient_email': SETTINGS.NHCP_ADMIN_MAIL,
                                                'booking_details_first_name': instance.name,
                                                'booking_details_mail': instance.email,
                                                'booking_details_service': instance.service,
                                                'booking_details_created_at': instance.created_at,
                                                'ref_link':f'http://{SETTINGS.IP_ADDRESS}:{SETTINGS.PORT}/booked_services',
                                                'model':'home_care_services'
                                            }
                                        )
        # Send the email
        try:
            send_mail_status = send_mail(
                'Home Care Service Booked',
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
            logging.error('e: ',e)
            logging.error("Email Sending Failed, Error in send_registration_mail() :{email_token}")
            return False
        



@receiver(post_save, sender=ServiceRegistrations) 
def notify_user(sender, instance, created, **kwargs):
    logging.info("in notify_admin")
    print("in notify_admin")
    print("instance.name: ",instance.name)
    print("link: ",'http://{SETTINGS.IP_ADDRESS}:{SETTINGS.PORT}/booked_services')
    if created:
        logging.info(F"sending mail to User")
        email_content = render_to_string('email_templates/home_care_lead_notify.html',
                                            {
                                                'mail_heading': 'New Home Care Service Booking',
                                                'mail_msg': 'You have received a new home care service booking',
                                                'recipient_name': 'NHCP Admin',
                                                'recipient_email': instance.email,
                                                'booking_details_first_name': instance.name,
                                                'booking_details_mail': instance.email,
                                                'booking_details_service': instance.service,
                                                'booking_details_created_at': instance.created_at,
                                                'ref_link':f'http://{SETTINGS.IP_ADDRESS}:{SETTINGS.PORT}/booked_services',
                                                'model':'home_care_services'
                                            }
                                        )
        # Send the email
        try:
            send_mail_status = send_mail(
                'Home Care Service Booked',
                email_content,
                SETTINGS.EMAIL_HOST_USER,  # Sender's email address
                [instance.email,],      # Recipient's email address
                # fail_silently=False,
                html_message=email_content,
            )
            logging.info(f"send_mail_status : {send_mail_status}")
            logging.info("Mail Sent Successfully to User")
            return True
        except Exception as e:
            logging.error('e: ',e)
            logging.error(f"Email Sending Failed, Error in send_registration_mail()")
            return False