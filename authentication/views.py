from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser, CountryDialCodes, Forgot_Password_Request
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from helper_views.authentication.send_signup_mail import send_registration_mail
from helper_views.authentication.generate_verify_mail_token import get_mail_from_token
from helper_views.authentication.send_forgot_password_mail import send_forgot_password_mail, decode_forgot_password_token, generate_forgot_password_token, reset_password_token_expired_or_not
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from django.utils import timezone
import logging

# log configuration
logging.basicConfig(
    format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='[%d/%b/%Y %H:%M:%S]')
# examples
# logging.info("Log Info Message")
# logging.warning("Log Warning Message")
# logging.error("Log Error Message")


def signup(request):
    if request.method=='POST':
        # try:
        if request.POST['full_name']:
            full_name = request.POST['full_name']
        if request.POST['email']:
            email = request.POST['email']
        if request.POST['hashedPassword']:
            password = request.POST['hashedPassword']
        if request.POST['phone_number']:
            user_phone_number = request.POST['phone_number']
        if request.POST['country']:
            country = request.POST['country']
        logging.info("{0} - User entered details full_name: {1}, email: {2}, password: {3}, phone number: {4}, country: {5}".format(email, full_name, email, password, user_phone_number, country))
        if CustomUser.objects.filter(email = email).exists():
            logging.warning('{0} - User already exists'.format(email))
            return HttpResponse('This email is already registered. Please use a different email')
        else:
            try:
                country_obj = CountryDialCodes.objects.get(country_name = country)
                logging.info(f"User Country {country}")
                try:
                    logging.info(f"user phone number: {user_phone_number}")
                    logging.info(f"user country: {country_obj}")
                    user = CustomUser.objects.create_user(email = email, password = password, username = full_name, phone_number = user_phone_number, country = country_obj)
                    # user.phone_number = phone_number
                    try:
                        user.save()
                        logging.info("{0} - User signed up successfully".format(email))
                        try:
                            logging.info("{0} - Email Sending Started".format(email))
                            send_registration_mail(email, full_name)
                        except Exception as e:
                            logging.info("{0} - Error in send_registration_mail()".format(email))
                            print('e: ',e)
                            return HttpResponse('Registration Mail not Sent')  
                        finally:
                            return HttpResponse('signup_success')
                    except Exception as e:
                        logging.error('e',e)
                        return HttpResponse("User Signup Failed, Try Again")
                except Exception as e:
                    print('e',e)
                    return HttpResponse('Something Went Wrong, Try Again')
            except Exception as e:
                print('e',e)
                logging.error("Can't Find Country Object")
                return HttpResponse('Something Went Wrong, Try Again')
        # except Exception as e:
        #     logging.error("Issue in getting Signup Form Data")
        #     logging.error(f'exception: {e}')
        #     return HttpResponse('Something Went Wrong, Try Again')
    else:
        logging.warning('Not post request')
        return render(request, 'signup.html')
    

def signin(request, reset_password_msg=None):
    if request.method=="POST":
        logging.info('in signin()')
        if request.POST['email']:
            email = request.POST['email']
        if request.POST['hashedPassword']:
            password = request.POST['hashedPassword']
        logging.info("{0} - User entered details email: {1} password: {2}".format(email,email,password))
        if CustomUser.objects.filter(email = email).exists():
            try:
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    logging.info("{0} - User Authenticated".format(email))
                    logging.info("{0} - User trying to signin".format(email))
                    try:
                        login(request, user)
                        logging.info("{0} - User signedin successfully".format(email))
                        # return redirect('index')
                        return HttpResponse('login_success')
                    except Exception as e:
                        logging.error(e)
                        logging.error("{0} - User can't login".format(email))
                        return HttpResponse('Something went wrong, Please try again')
                else:
                    logging.error('{0} - Email or Password is Incorrect'.format(email))
                    return HttpResponse('Incorrect Email or Password. Please try again')
            except Exception as e:
                logging.error(e)
                logging.error('{0} - Something went wrong'.format(email))
                return HttpResponse('Something went wrong, Please try again')
        else:
            logging.error('{0} - User not found, Please Sign Up'.format(email))
            return HttpResponse("No account found for this email. Please verify email or sign up") 
    elif reset_password_msg != None:
        logging.info(f'reset password msg: {reset_password_msg}')  
        return render(request, 'signin.html',{'reset_password_msg':reset_password_msg})
    else:
        logging.warning('Not post request')
        return render(request, 'signin.html') 


# note: the parameter name should be same as the value in url pattern
def verify_mail(request, token):
    logging.info(f"Verifying Mail, token: {token}")
    try:
        user_mail = get_mail_from_token(token)
        if user_mail:
            logging.info(f"User Mail from Token: {user_mail}")
            try:
                user_obj = CustomUser.objects.get(email = user_mail)
                logging.info(f"User {user_mail} trying to Verify Mail")
                user_obj.is_mail_verified = True
                user_obj.save()
                if request.user.is_authenticated:
                    return render(request, 'index.html', {'verify_mail_sucess_message':'Mail Verified Successfully'})
                else:
                    return render(request, 'signin.html', {'verify_mail_sucess_message':'Mail Verified Successfully'})
            except Exception as e:
                logging.error(e)
                logging.error("Can't Find User Object while verifying Mail")
                return render(request, 'signin.html')
        else:
            return render(request, 'signin.html', {'verify_mail_failure_message':"Can't Verify Mail, Try Again"})
    except Exception as e:
                logging.error(e)
                logging.error("Can't Find Mail form Verify Mail Token")
                return render(request, 'signin.html', {'verify_mail_failure_message':"Can't Verify Mail, Try Again"})
    

# error messages in forgot password page when this page is rendered from the reset password page
# error_msg param is error message of the forgot password page
def forgot_password_page(request, error_msg=None):
    logging.info('in forgot_password_page')
    if request.method=="POST":
        email = request.POST['email']
        logging.info(f'Email entered for Forgot Password Request: {email}')
        try:
            user_obj = CustomUser.objects.get(email = email)
            logging.info(f'User Object with above email: {user_obj}')
            username = user_obj.username
            logging.info(f'Username: {username}')

            creat_new_forgot_password_request = False
            delete_existing_forgot_password_request = False

            logging.info(f'checking if the user has any forgot password request existing or not')
            # checking if the user has any forgot password request existing or not
            if Forgot_Password_Request.objects.filter(user = user_obj).exists():
                logging.info(f'Forgot Password Request already Exists for User {user_obj}')
                user_forgot_password_req = Forgot_Password_Request.objects.get(user = user_obj)
                # Calculate the expiration time (24 hours from the timestamp)
                expiration_time = user_forgot_password_req.timestamp + timezone.timedelta(minutes=10)
                # Get the current time
                current_time = timezone.now()
                # checking if the existing forgot password object expired or not
                if current_time > expiration_time:
                    # forgot password request object expired
                    creat_new_forgot_password_request = True
                    delete_existing_forgot_password_request = True
                    logging.info(f'Existing Forgot Password Request is Expired for user: {user_forgot_password_req}')
                else:
                    logging.info(f'Existing Forgot Password Request not Expired for user: {user_forgot_password_req}')
                    # forgot password request object not expired
                    try:
                        # logging.info(f'Generating Token for Forgot Password Request')
                        # user_forgot_password_req
                        # token = generate_forgot_password_token(email)
                        try:
                            logging.info(f'Generating Token for Forgot Password Request')
                            logging.info(f'Sending Mail for Forgot Password Request with Existing Token')
                            #sending mail with existing token
                            mail_status = send_forgot_password_mail(email, username, user_forgot_password_req.token, expiration_time)
                            # return render(request, 'forgot.html', {'forgot_password_mail_success':"Reset Password Link Sent, Kindly Check Your Mail"})
                            logging.info(f"mail_status: {mail_status}")
                            if mail_status:
                                return HttpResponse('forgot_password_success')
                            else:
                                return HttpResponse("Can't Send Mail, Try Again")
                        except Exception as e:
                            logging.error(f'e: {e}')
                            logging.error("Can't Send Forgot Password Mail")
                            # return render(request, 'forgot.html', {'forgot_password_mail_failure':"Something Went Wrong, Try Again"})
                            return HttpResponse('Something Went Wrong, Try Again')
                    except Exception as e:
                        logging.error(f'e: {e}')
                        logging.error("Can't Generate Forgot Password Token")
                        # return render(request, 'forgot.html', {'forgot_password_mail_failure':"Something Went Wrong, Try Again"})
                        return HttpResponse('Something Went Wrong, Try Again')
            else:
                logging.info(f"Forgot Password Request doesn't Exists for User {user_obj}")
                creat_new_forgot_password_request = True
            if creat_new_forgot_password_request:
                if delete_existing_forgot_password_request:
                    logging.info(f"Deleting Existing Forgot Password Request for User {user_obj}")
                    # fetching existing forgot password request
                    user_forgot_password_req = Forgot_Password_Request.objects.get(user = user_obj)
                    # deleting existing forgot password request
                    user_forgot_password_req.delete()
                try:
                    logging.info(f'Generating Token for Forgot Password Request')
                    reset_password_token  = generate_forgot_password_token(user_obj.email)
                    try:
                        logging.info(f"Generating Forgot Password Request for User {user_obj}")

                        # creating new forgot password request 
                        forgot_password_obj = Forgot_Password_Request()
                        forgot_password_obj.user = user_obj
                        forgot_password_obj.token = reset_password_token
                        forgot_password_obj.save()
                        try:
                            expiry_time = timezone.now() + timezone.timedelta(hours=1)
                            logging.info(f'Sending Forgot Password Mail for {user_obj}')
                            #sending forgot password mail
                            mail_status = send_forgot_password_mail(email, username, reset_password_token, expiry_time)
                            # return render(request, 'forgot.html', {'forgot_password_mail_success':"Reset Password Link Sent, Kindly Check Your Mail"})
                            logging.info(f"mail_status: {mail_status}",)
                            if mail_status:
                                return HttpResponse('forgot_password_success')
                            else:
                                return HttpResponse("Can't Send Mail, Try Again")
                        except Exception as e:
                            logging.error(f'e: {e}')
                            logging.error("Can't Send Forgot Password Mail")
                            # return render(request, 'forgot.html', {'forgot_password_mail_failure':"Something Went Wrong, Try Again"})
                            return HttpResponse('Something Went Wrong, Try Again')
                    except Exception as e:
                        logging.error(f'e: {e}')
                        logging.error("Can't Create Forgot Password Request")
                        # return render(request, 'forgot.html', {'forgot_password_mail_failure':"Something Went Wrong, Try Again"})
                        return HttpResponse('Something Went Wrong, Try Again')
                except Exception as e:
                    logging.error(f'e: {e}')
                    logging.error("Can't Generate Forgot Password Token")
                    # return render(request, 'forgot.html', {'forgot_password_mail_failure':"Something Went Wrong, Try Again"})
                    return HttpResponse('Something Went Wrong, Try Again')
        except ObjectDoesNotExist:
            logging.error("Can't Send Forgot Password Mail as Email not Registered")
            # return render(request, 'forgot.html', {'forgot_password_mail_failure':"Email not Registered, Try with Registered Mail"})
            return HttpResponse('Email not Registered')
        except Exception as e:
            logging.error(f'e: {e}')
            logging.error("Can't Send Forgot Password Mail")
            # return render(request, 'forgot.html', {'forgot_password_mail_failure':"Something Went Wrong, Try Again"})
            return HttpResponse('Something Went Wrong, Try Again')
    elif error_msg!=None:
        logging.info(f'error msg: {error_msg}')  
        return render(request, 'forgot.html',{'forgot_password_mail_failure':error_msg})
    else: 
        logging.info(f'GET request for forgot_password_page()')  
        return render(request, 'forgot.html')


def reset_password(request, token):
    logging.info("in reset_password")
    if request.method=="POST":
        if Forgot_Password_Request.objects.filter(token = token).exists():
            forgot_password_request_obj = Forgot_Password_Request.objects.get(token = token)
            logging.info(f'Reset Password Token Received: {token}')
            token_expired_or_not = reset_password_token_expired_or_not(token)
            if token_expired_or_not == 'Reset Password Token not Expired':
                new_password = request.POST['new_password']
                new_confirm_password = request.POST['new_confirm_password']
                logging.info(f'User Reset Password new_password: {new_password} new_confirm_password: {new_confirm_password}')
                if new_password == new_confirm_password:
                    if forgot_password_request_obj:
                        logging.info(f'Resetting Password for Forgot Password Request: {forgot_password_request_obj}')
                        user_obj = forgot_password_request_obj.user
                        user_obj.set_password(new_password)
                        user_obj.save()
                        forgot_password_request_obj.delete()
                        return HttpResponse('Password Reset Successful')
                        # return render(request, 'index.html', {'verify_mail_sucess_message':'Password Reset Successful'})
                    else:
                        logging.error(f"Forgot Password Request Object doesn't exist")
                        return render(request, 'forgot.html', {'forgot_password_mail_failure':"Something Went Wrong, Try Again With Link Sent In The Mail"})  
                else:
                    logging.error(f"New Password and New Confirm Password are not Equal")
                    return render(request, 'reset.html', {'reset_password_failure':"Password and Confirm Password are not Equal"})
            elif token_expired_or_not == "Can't Decode Token, Try Again":
                return render(request, 'reset_password_invalid_token.html',{'msg':"Can't Decode Link, Try Again With Link Sent In The Mail"})
            elif (token_expired_or_not == 'Token has expired') or (token_expired_or_not == 'Reset Password Token Expired'):
                return HttpResponse('Reset Password Link Expired, Try Again')
                # return render(request, 'forgot.html', {'forgot_password_mail_failure':"Reset Password Link Expired, Try Again"})
            elif token_expired_or_not == "Can't Decode Token, Try Again":
                return render(request, 'reset_password_invalid_token.html',{'msg':"Can't Decode Link, Try Again With Link Sent In The Mail"})
            elif token_expired_or_not == "Link Doesn't Exists, May be Link has been used already. Please Request a new password reset":
                return render(request, 'reset_password_invalid_token.html',{'msg':"Link Doesn't Exists, May be Link has been used already. Please Request a new password reset"})
            else:
                logging.error(f'Something Went Wrong')
                return render(request, 'forgot.html', {'forgot_password_mail_failure':"Something Went Wrong, Try Again"})
        else:
            logging.info("Forgot Password Request token doesn't Exists")
            return render(request, 'forgot.html',{'forgot_password_mail_failure':"Link Doesn't Exists, May be Used Already. Please Request a new password reset"})
    else:
        if Forgot_Password_Request.objects.filter(token = token).exists():
            forgot_password_request_obj = Forgot_Password_Request.objects.get(token = token)
            token_expired_or_not = reset_password_token_expired_or_not(token)
            if token_expired_or_not == 'Reset Password Token not Expired':
                logging.info('Reset Password Token not Expired')
                return render(request, 'reset.html')
            elif token_expired_or_not == "Invalid Token":
                logging.info("Invalid Token")
                return render(request, 'reset_password_invalid_token.html',{'msg':'Invalid Link, Try Again With Link Sent In The Mail'})
            elif token_expired_or_not == "Can't Decode Token, Try Again":
                logging.info("Can't Decode Token, Try Again")
                return render(request, 'reset_password_invalid_token.html',{'msg':"Can't Decode Link, Try Again With Link Sent In The Mail"})
            elif (token_expired_or_not == 'Reset Password Token Expired'):
                logging.info('Token has expired')
                # if render() is used then forgot.html is rendering but the url is not changing to forgot_password_page instead it is 
                # being http://127.0.0.1:8000/auth/reset_password/token
                # return render(request, 'forgot.html', {'forgot_password_mail_failure':"Reset Password Link Expired, Try Again"})
                # below redirect will hit the dynamic url of forgot_password_page 
                # ie., path('forgot_password_page/<str:error_msg>', views.forgot_password_page, name = 'forgot_password_page'), 
                return redirect('forgot_password_page', error_msg='Reset Password Link Expired, Try Again')
            else:
                logging.info('Something Went Wrong, Try Again')
                return render(request, 'forgot.html', {'forgot_password_mail_failure':"Something Went Wrong, Try Again"})
        else:
            logging.info("Can't Decode Token, Try Again")
            return render(request, 'forgot.html',{'forgot_password_mail_failure':"Link Doesn't Exists, May be Used Already. Please Request a new password reset"})



def reset_password_invalid_token(request):
    # print('in reset_password_invalid_token')
    return render(request, 'reset_password_invalid_token.html')


@login_required(login_url='/auth/signin')
def signout(request):
    try: 
        user_email = request.user.email
        logout(request)
        logging.info("{0} - User logged out successfully".format(user_email))
        return redirect('/auth/signin')
    except Exception as e:
        logging.error(e)
        logging.error("{0} - User logout failed".format(user_email))
        return redirect('/auth/signin')

