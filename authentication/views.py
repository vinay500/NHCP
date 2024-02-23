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


# def save_country_data(request):
#     allCountries = [
#         ['Afghanistan', 'AF', '93'],
#         ['Albania', 'AL', '355'],
#         ['Algeria', 'DZ', '213'],
#         ['American Samoa', 'AS', '1'],
#         ['Andorra', 'AD', '376'],
#         ['Angola', 'AO', '244'],
#         ['Anguilla', 'AI', '1'],
#         ['Antigua and Barbuda', 'AG', '1'],
#         ['Argentina', 'AR', '54'],
#         ['Armenia', 'AM', '374'],
#         ['Aruba', 'AW', '297'],
#         ['Ascension', 'AC', '247'],
#         ['Australia', 'AU', '61'],
#         ['Austria', 'AT', '43'],
#         ['Azerbaijan', 'AZ', '994'],
#         ['Bahamas', 'BS', '1'],
#         ['Bahrain', 'BH', '973'],
#         ['Bangladesh', 'BD', '880'],
#         ['Barbados', 'BB', '1'],
#         ['Belarus', 'BY', '375'],
#         ['Belgium', 'BE', '32'],
#         ['Belize', 'BZ', '501'],
#         ['Benin', 'BJ', '229'],
#         ['Bermuda', 'BM', '1'],
#         ['Bhutan', 'BT', '975'],
#         ['Bolivia', 'BO', '591'],
#         ['Bosnia and Herzegovina', 'BA', '387'],
#         ['Botswana', 'BW', '267'],
#         ['Brazil', 'BR', '55'],
#         ['British Indian Ocean Territory', 'IO', '246'],
#         ['British Virgin Islands', 'VG', '1'],
#         ['Brunei', 'BN', '673'],
#         ['Bulgaria', 'BG', '359'],
#         ['Burkina Faso', 'BF', '226'],
#         ['Burundi', 'BI', '257'],
#         ['Cambodia', 'KH', '855'],
#         ['Cameroon', 'CM', '237'],
#         ['Canada', 'CA', '1'],
#         ['Cape Verde', 'CV', '238'],
#         ['Caribbean Netherlands', 'BQ', '599'],
#         ['Cayman Islands', 'KY', '1'],
#         ['Central African Republic', 'CF', '236'],
#         ['Chad', 'TD', '235'],
#         ['Chile', 'CL', '56'],
#         ['China', 'CN', '86'],
#         ['Christmas Island', 'CX', '61'],
#         ['Cocos (Keeling) Islands', 'CC', '61'],
#         ['Colombia', 'CO', '57'],
#         ['Comoros', 'KM', '269'],
#         ['Congo (DRC)', 'CD', '243'],
#         ['Congo (Republic)', 'CG', '242'],
#         ['Cook Islands', 'CK', '682'],
#         ['Costa Rica', 'CR', '506'],
#         ["Côte d'Ivoire", 'CI', '225'],
#         ['Croatia', 'HR', '385'],
#         ['Cuba', 'CU', '53'],
#         ['Curaçao', 'CW', '599'],
#         ['Cyprus', 'CY', '357'],
#         ['Czech Republic', 'CZ', '420'],
#         ['Denmark', 'DK', '45'],
#         ['Djibouti', 'DJ', '253'],
#         ['Dominica', 'DM', '1'],
#         ['Dominican Republic', 'DO', '1'],
#         ['Ecuador', 'EC', '593'],
#         ['Egypt', 'EG', '20'],
#         ['El Salvador', 'SV', '503'],
#         ['Equatorial Guinea', 'GQ', '240'],
#         ['Eritrea', 'ER', '291'],
#         ['Estonia', 'EE', '372'],
#         ['Eswatini', 'SZ', '268'],
#         ['Ethiopia', 'ET', '251'],
#         ['Falkland Islands', 'FK', '500'],
#         ['Faroe Islands', 'FO', '298'],
#         ['Fiji', 'FJ', '679'],
#         ['Finland', 'FI', '358'],
#         ['France', 'FR', '33'],
#         ['French Guiana', 'GF', '594'],
#         ['French Polynesia', 'PF', '689'],
#         ['Gabon', 'GA', '241'],
#         ['Gambia', 'GM', '220'],
#         ['Georgia', 'GE', '995'],
#         ['Germany', 'DE', '49'],
#         ['Ghana', 'GH', '233'],
#         ['Gibraltar', 'GI', '350'],
#         ['Greece', 'GR', '30'],
#         ['Greenland', 'GL', '299'],
#         ['Grenada', 'GD', '1'],
#         ['Guadeloupe', 'GP', '590'],
#         ['Guam', 'GU', '1'],
#         ['Guatemala', 'GT', '502'],
#         ['Guernsey', 'GG', '44'],
#         ['Guinea', 'GN', '224'],
#         ['Guinea-Bissau', 'GW', '245'],
#         ['Guyana', 'GY', '592'],
#         ['Haiti', 'HT', '509'],
#         ['Honduras', 'HN', '504'],
#         ['Hong Kong', 'HK', '852'],
#         ['Hungary', 'HU', '36'],
#         ['Iceland', 'IS', '354'],
#         ['India', 'IN', '91'],
#         ['Indonesia', 'ID', '62'],
#         ['Iran', 'IR', '98'],
#         ['Iraq', 'IQ', '964'],
#         ['Ireland', 'IE', '353'],
#         ['Isle of Man', 'IM', '44'],
#         ['Israel', 'IL', '972'],
#         ['Italy', 'IT', '39'],
#         ['Jamaica', 'JM', '1'],
#         ['Japan', 'JP', '81'],
#         ['Jersey', 'JE', '44'],
#         ['Jordan', 'JO', '962'],
#         ['Kazakhstan', 'KZ', '7'],
#         ['Kenya', 'KE', '254'],
#         ['Kiribati', 'KI', '686'],
#         ['Kosovo', 'XK', '383'],
#         ['Kuwait', 'KW', '965'],
#         ['Kyrgyzstan', 'KG', '996'],
#         ['Laos', 'LA', '856'],
#         ['Latvia', 'LV', '371'],
#         ['Lebanon', 'LB', '961'],
#         ['Lesotho', 'LS', '266'],
#         ['Liberia', 'LR', '231'],
#         ['Libya', 'LY', '218'],
#         ['Liechtenstein', 'LI', '423'],
#         ['Lithuania', 'LT', '370'],
#         ['Luxembourg', 'LU', '352'],
#         ['Macau', 'MO', '853'],
#         ['North Macedonia', 'MK', '389'],
#         ['Madagascar', 'MG', '261'],
#         ['Malawi', 'MW', '265'],
#         ['Malaysia', 'MY', '60'],
#         ['Maldives', 'MV', '960'],
#         ['Mali', 'ML', '223'],
#         ['Malta', 'MT', '356'],
#         ['Marshall Islands', 'MH', '692'],
#         ['Martinique', 'MQ', '596'],
#         ['Mauritania', 'MR', '222'],
#         ['Mauritius', 'MU', '230'],
#         ['Mayotte', 'YT', '262'],
#         ['Mexico', 'MX', '52'],
#         ['Micronesia', 'FM', '691'],
#         ['Moldova', 'MD', '373'],
#         ['Monaco', 'MC', '377'],
#         ['Mongolia', 'MN', '976'],
#         ['Montenegro', 'ME', '382'],
#         ['Montserrat', 'MS', '1'],
#         ['Morocco', 'MA', '212'],
#         ['Mozambique', 'MZ', '258'],
#         ['Myanmar (Burma)', 'MM', '95'],
#         ['Namibia', 'NA', '264'],
#         ['Nauru', 'NR', '674'],
#         ['Nepal', 'NP', '977'],
#         ['Netherlands', 'NL', '31'],
#         ['New Caledonia', 'NC', '687'],
#         ['New Zealand', 'NZ', '64'],
#         ['Nicaragua', 'NI', '505'],
#         ['Niger', 'NE', '227'],
#         ['Nigeria', 'NG', '234'],
#         ['Niue', 'NU', '683'],
#         ['Norfolk Island', 'NF', '672'],
#         ['North Korea', 'KP', '850'],
#         ['Northern Mariana Islands', 'MP', '1'],
#         ['Norway', 'NO', '47'],
#         ['Oman', 'OM', '968'],
#         ['Pakistan', 'PK', '92'],
#         ['Palau', 'PW', '680'],
#         ['Palestine', 'PS', '970'],
#         ['Panama', 'PA', '507'],
#         ['Papua New Guinea', 'PG', '675'],
#         ['Paraguay', 'PY', '595'],
#         ['Peru', 'PE', '51'],
#         ['Philippines', 'PH', '63'],
#         ['Poland', 'PL', '48'],
#         ['Portugal', 'PT', '351'],
#         ['Puerto Rico', 'PR', '1'],
#         ['Qatar', 'QA', '974'],
#         ['Réunion', 'RE', '262'],
#         ['Romania', 'RO', '40'],
#         ['Russia', 'RU', '7'],
#         ['Rwanda', 'RW', '250'],
#         ['Saint Barthélemy', 'BL', '590'],
#         ['Saint Helena', 'SH', '290'],
#         ['Saint Kitts and Nevis', 'KN', '1'],
#         ['Saint Lucia', 'LC', '1'],
#         ['Saint Martin', 'MF', '590'],
#         ['Saint Pierre and Miquelon', 'PM', '508'],
#         ['Saint Vincent and the Grenadines', 'VC', '1'],
#         ['Samoa', 'WS', '685'],
#         ['San Marino', 'SM', '378'],
#         ['São Tomé and Príncipe', 'ST', '239'],
#         ['Saudi Arabia', 'SA', '966'],
#         ['Senegal', 'SN', '221'],
#         ['Serbia', 'RS', '381'],
#         ['Seychelles', 'SC', '248'],
#         ['Sierra Leone', 'SL', '232'],
#         ['Singapore', 'SG', '65'],
#         ['Sint Maarten', 'SX', '1'],
#         ['Slovakia', 'SK', '421'],
#         ['Slovenia', 'SI', '386'],
#         ['Solomon Islands', 'SB', '677'],
#         ['Somalia', 'SO', '252'],
#         ['South Africa', 'ZA', '27'],
#         ['South Korea', 'KR', '82'],
#         ['South Sudan', 'SS', '211'],
#         ['Spain', 'ES', '34'],
#         ['Sri Lanka', 'LK', '94'],
#         ['Sudan', 'SD', '249'],
#         ['Suriname', 'SR', '597'],
#         ['Svalbard and Jan Mayen', 'SJ', '47'],
#         ['Sweden', 'SE', '46'],
#         ['Switzerland', 'CH', '41'],
#         ['Syria', 'SY', '963'],
#         ['Taiwan', 'TW', '886'],
#         ['Tajikistan', 'TJ', '992'],
#         ['Tanzania', 'TZ', '255'],
#         ['Thailand', 'TH', '66'],
#         ['Timor-Leste', 'TL', '670'],
#         ['Togo', 'TG', '228'],
#         ['Tokelau', 'TK', '690'],
#         ['Tonga', 'TO', '676'],
#         ['Trinidad and Tobago', 'TT', '1'],
#         ['Tunisia', 'TN', '216'],
#         ['Turkey', 'TR', '90'],
#         ['Turkmenistan', 'TM', '993'],
#         ['Turks and Caicos Islands', 'TC', '1'],
#         ['Tuvalu', 'TV', '688'],
#         ['U.S. Virgin Islands', 'VI', '1'],
#         ['Uganda', 'UG', '256'],
#         ['Ukraine', 'UA', '380'],
#         ['United Arab Emirates', 'AE', '971'],
#         ['United Kingdom', 'GB', '44'],
#         ['United States', 'US', '1'],
#         ['Uruguay', 'UY', '598'],
#         ['Uzbekistan', 'UZ', '998'],
#         ['Vanuatu', 'VU', '678'],
#         ['Vatican City', 'VA', '39'],
#         ['Venezuela', 'VE', '58'],
#         ['Vietnam', 'VN', '84'],
#         ['Wallis and Futuna', 'WF', '681'],
#         ['Western Sahara', 'EH', '212'],
#         ['Yemen', 'YE', '967'],
#         ['Zambia', 'ZM', '260'],
#         ['Zimbabwe', 'ZW', '263'],
#         ['Åland Islands', 'AX', '358']
#     ]

#     for country in allCountries:
#         print('country name',country[0])
#         print('country_short_form',country[1])
#         print('country_dial_code',country[2])
#         try:
#             country_details =  CountryDialCodes()
#             country_details.country_name = country[0]
#             country_details.country_short_form = country[1]
#             country_details.country_dial_code = country[2]
#             country_details.save()
#         except Exception as e:
#             print('erron in save_country_data(): ',e)
#             return HttpResponse("erron in save_country_data()")
#     return HttpResponse("country details saved succesfully")



def signup(request):
    if request.method=='POST':
        if request.POST['full_name']:
            full_name = request.POST['full_name']
        if request.POST['email']:
            email = request.POST['email']
        if request.POST['hashedPassword']:
            password = request.POST['hashedPassword']
        if request.POST['phone_number']:
            phone_number = request.POST['phone_number']
        if request.POST['country']:
            country = request.POST['country']
        logging.info("{0} - User entered details full_name: {1}, email: {2}, password: {3}, phone number: {4}, country: {5}".format(email,full_name,email,password,phone_number,country))
        if CustomUser.objects.filter(email = email).exists():
            logging.warning('{0} - User already exists'.format(email))
            return HttpResponse('This email is already registered. Please use a different email')
        else:
            try:
                country = CountryDialCodes.objects.get(country_name = country)
                logging.info(f"User Country {country}")
                try:
                    user = CustomUser.objects.create_user(email = email, password = password, username = full_name, phone_number = phone_number, country = country)
                    # user.phone_number = phone_number
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
                    print('e',e)
                    return HttpResponse('Something Went Wrong, Try Again')
            except Exception as e:
                print('e',e)
                logging.error("Can't Find Country Object")
                return HttpResponse('Something Went Wrong, Try Again')
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
    elif reset_password_msg!=None:
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
                            send_forgot_password_mail(email, username, user_forgot_password_req.token, expiration_time)
                            # return render(request, 'forgot.html', {'forgot_password_mail_success':"Reset Password Link Sent, Kindly Check Your Mail"})
                            return HttpResponse('forgot_password_success')
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
                            send_forgot_password_mail(email, username, reset_password_token, expiry_time)
                            # return render(request, 'forgot.html', {'forgot_password_mail_success':"Reset Password Link Sent, Kindly Check Your Mail"})
                            return HttpResponse('forgot_password_success')
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
    if request.method=="POST":
        logging.info(f'Reset Password Token Received: {token}')
        token_expired_or_not = reset_password_token_expired_or_not(token)
        if token_expired_or_not == 'Reset Password Token not Expired':
            new_password = request.POST['new_password']
            new_confirm_password = request.POST['new_confirm_password']
            logging.info(f'User Reset Password new_password: {new_password} new_confirm_password: {new_confirm_password}')
            if new_password == new_confirm_password:
                forgot_password_request_obj = Forgot_Password_Request.objects.get(token = token)
                if forgot_password_request_obj:
                    logging.info(f'Resetting Password for Forgot Password Request: {forgot_password_request_obj}')
                    user_obj = forgot_password_request_obj.user
                    user_obj.set_password(new_password)
                    user_obj.save()
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
        else:
            logging.error(f'Something Went Wrong')
            return render(request, 'forgot.html', {'forgot_password_mail_failure':"Something Went Wrong, Try Again"})
    else:
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
            # return render(request, 'forgot.html', {'forgot_password_mail_failure':"Reset Password Link Expired, Try Again"})
            # return HttpResponse('Reset Password Link Expired, Try Again')
            # below redirect will hit the dynamic url of forgot_password_page 
            # ie., path('forgot_password_page/<str:error_msg>', views.forgot_password_page, name = 'forgot_password_page'), 
            return redirect('forgot_password_page', error_msg='Reset Password Link Expired, Try Again')
        else:
            logging.info('Something Went Wrong, Try Again')
            return render(request, 'forgot.html', {'forgot_password_mail_failure':"Something Went Wrong, Try Again"})



def reset_password_invalid_token(request):
    # print('in reset_password_invalid_token')
    return render(request, 'reset_password_invalid_token.html')


@login_required(login_url='signin')
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

# # Signals


# @receiver(models.signals.post_save, sender=User)
# def do_something(sender, instance, created, **kwargs):
#     print('in post_save function of user model')