from datetime import datetime, timedelta
from django.conf import settings as SETTINGS
from django.core.mail import send_mail
from django.template.loader import render_to_string
import logging
import jwt


logging.basicConfig(
    format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='[%d/%b/%Y %H:%M:%S]')


def generate_forgot_password_token(user_email):
    logging.info("in generate_encrypted_token")
    
    # Set the expiration time to 24 hours from now
    expiration_time = datetime.utcnow() + timedelta(minutes=3)
    
    # Convert the expiration time to a Unix timestamp
    expiration_timestamp = int(expiration_time.timestamp())
    
    # Create the payload with email and expiration time
    payload = {'email': user_email, 'exp': expiration_timestamp}
    
    # Encode the payload into a token
    token = jwt.encode(payload, SETTINGS.EMAIL_VERIFICATION_SECRET_KEY, algorithm='HS256')
    logging.info(f'token: {token}')
    
    return token, expiration_time


def decode_forgot_password_token(token):
    try:
        # Decode the token
        decoded_payload = jwt.decode(token, SETTINGS.EMAIL_VERIFICATION_SECRET_KEY, algorithms=['HS256'])
        
        # Extract email and expiration time from the decoded payload
        email = decoded_payload['email']
        expiration_timestamp = decoded_payload['exp']
        # Convert expiration timestamp back to datetime
        expiration_timestamp_in_datetime = datetime.utcfromtimestamp(expiration_timestamp)
        return email, expiration_timestamp_in_datetime
    except Exception as e:
        logging.error(f"Error in get_mail_from_token(), error: {e}")
        return None
    

def send_forgot_password_mail(recipient_email, recipient_name):
    logging.info('in send_forgot_password_mail()')
    logging.info(F"Generating Token for Forgot Password")
    email_token = generate_forgot_password_token(recipient_email)
    logging.info(F"email_token in send_registration_mail: {email_token}")
    email_content = render_to_string('forgot_password.html',
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
        print('e: ',e)
        logging.error("Email Sending Failed, Error in send_registration_mail() :{email_token}")
        # return HttpResponse('Email sent successfully!')
        return False



