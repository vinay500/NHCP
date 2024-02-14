from django.conf import settings
import logging
import jwt


def generate_encrypted_token(user_email):
    logging.info("in generate_encrypted_token")
    payload = {'email': user_email}
    token = jwt.encode(payload, settings.EMAIL_VERIFICATION_SECRET_KEY, algorithm='HS256')
    logging.info(f'token: {token}')
    return token


def get_mail_from_token(token):
    try:
        decoded_payload = jwt.decode(token, settings.EMAIL_VERIFICATION_SECRET_KEY, algorithms=['HS256'])
        email = decoded_payload['email']
        return email
    except Exception as e:
        logging.error(f"Error in get_mail_from_token(),error: {e}")
        return None
    