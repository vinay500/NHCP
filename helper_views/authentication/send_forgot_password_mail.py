from datetime import datetime, timedelta, timezone
from smtplib import SMTPAuthenticationError
from django.conf import settings as SETTINGS
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError, DecodeError, InvalidSignatureError
from authentication.models import Forgot_Password_Request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
import jwt
import smtplib




logging.basicConfig(
    format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='[%d/%b/%Y %H:%M:%S]')



def generate_forgot_password_token(user_email):
    logging.info("in generate_encrypted_token")
    django_timezone = timezone.get_default_timezone()
    # Set the expiration time to 24 hours from now
    expiration_time = timezone.now() + timedelta(minutes=10)
    logging.info(f'Current time {datetime.utcnow()}')
    logging.info(f'token expiration_time {expiration_time}')
    logging.info(f' type: token expiration_time {type(expiration_time)}')
    # Convert the expiration time to a Unix timestamp
    expiration_timestamp = int(expiration_time.timestamp())
    
    # Create the payload with email and expiration time
    payload = {'email': user_email, 'token_expiry_time': expiration_timestamp}
    # payload = {'email': user_email}
    
    # Encode the payload into a token
    token = jwt.encode(payload, SETTINGS.EMAIL_VERIFICATION_SECRET_KEY, algorithm='HS256')
    logging.info(f'token: {token}')
    
    return token


def decode_forgot_password_token(token):
    try:
        logging.info(f'Decoding the Token {token}')
        # Decode the token
        decoded_payload = jwt.decode(token, SETTINGS.EMAIL_VERIFICATION_SECRET_KEY, algorithms=['HS256'])
        logging.info(f'Token Payload: {decoded_payload}')
        return decoded_payload
    # a signature is a piece of data generated by applying a cryptographic algorithm to the header and payload of the JWT 
    # along with a secret key. The signature is used to verify the integrity of the JWT and ensure that it has not been tampered with 
    # during transmission.
    except InvalidTokenError or DecodeError or InvalidSignatureError:
        logging.error(f"Invalid Token")
        return "Invalid Token"
    except Exception as e:
        logging.error(f"Error in get_mail_from_token(), error: {e}")
        return "Can't Decode Token, Try Again"
    

def send_forgot_password_mail(recipient_email, recipient_name, token, expiry_time):
    logging.info(F"Generating Token for Forgot Password")
    logging.info(F"email_token in send_registration_mail: {token}")

    #------------------ sending mail with gmail -------------------------------
    # email_content = render_to_string('forgot_password.html',
    #                                     {
    #                                         'recipient_name': recipient_name,
    #                                         'recipient_email': recipient_email,
    #                                         'email_token': token,
    #                                         'IP_ADDRESS': SETTINGS.IP_ADDRESS,
    #                                         'PORT': SETTINGS.PORT,
    #                                         'expiry_time': expiry_time,
    #                                     }
    #                                 )
    # # Send the email
    # try:
    #     # raise Exception("testing logging for forgot password mail")
    #     send_mail_status = send_mail(
    #         'Welcome to Swasth Medical Associates',
    #         email_content,
    #         SETTINGS.EMAIL_HOST_USER,  # Sender's email address
    #         [recipient_email],      # Recipient's email address
    #         # fail_silently=False,
    #         html_message=email_content,
    #     )


    #------------------ sending mail with hostinger mail -------------------------------
    subject = "Reset Your Password"
    html_content = render_to_string('forgot_password.html',
                                        {
                                            'recipient_name': recipient_name,
                                            'recipient_email': recipient_email,
                                            'email_token': token,
                                            'IP_ADDRESS': SETTINGS.IP_ADDRESS,
                                            'PORT': SETTINGS.PORT,
                                            'expiry_time': expiry_time,
                                        }
                                    )

    # Create the email
    msg = MIMEMultipart("alternative")
    msg['From'] = SETTINGS.EMAIL_HOST_USER
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the HTML content
    msg.attach(MIMEText(html_content, "html"))

    # Send the email
    try:
        server = smtplib.SMTP(SETTINGS.EMAIL_HOST, SETTINGS.EMAIL_PORT)
        server.starttls()
        server.login(SETTINGS.EMAIL_HOST_USER, SETTINGS.EMAIL_HOST_PASSWORD)
        server.sendmail(SETTINGS.EMAIL_HOST_USER, recipient_email, msg.as_string())
        server.quit()
        # logging.info(f"send_mail_status : {send_mail_status}")
        logging.info("User Registration Mail Sent Successfully")
        return True
    except SMTPAuthenticationError as e:
        logging.error(f"exception: {e}")
        logging.error("Email Sending Failed, SMTPAuthenticationError")
        return False
    except Exception as e:
        logging.error(f"exception: {e}")
        logging.error("Email Sending Failed, Error in send_registration_mail()")
        return False
    


def reset_password_token_expired_or_not(token):
    django_timezone = timezone.get_default_timezone()
    logging.info(f'Reset Password Token Received: {token}')
    token_decoded_value = decode_forgot_password_token(token)
    logging.info(f'token_decoded_value: {token_decoded_value}') 
    if token_decoded_value == 'Invalid Token':
        return "Invalid Token"
    elif token_decoded_value == "Can't Decode Token, Try Again":
        return "Can't Decode Token, Try Again"
    else:
        user_mail, expiry_timestamp = token_decoded_value['email'], token_decoded_value['token_expiry_time']
        logging.info(f'User Mail and Expiry Timestamp from Token: {user_mail}, {expiry_timestamp}')
        # current_time = datetime.utcnow()
        current_time = timezone.now()
        logging.info(f'Current Time {current_time}')
        expiration_time_from_timestamp = timezone.datetime.fromtimestamp(expiry_timestamp, django_timezone)
        # Format the datetime object as a string (adjust the format as needed)
        formatted_datetime = expiration_time_from_timestamp.strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"expiry time from timestamp: {formatted_datetime}")
        logging.info(f"int(current_time.timestamp()): {int(current_time.timestamp())}")
        if int(current_time.timestamp()) > int(expiration_time_from_timestamp.timestamp()):
            logging.error(f'Reset Password Token Expired: {token}')
            return 'Reset Password Token Expired'
        else:
            logging.info(f'Reset Password Token not Expired: {token}')
            return 'Reset Password Token not Expired'




