from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings as SETTINGS
from django.http import HttpResponse
from .models import BeyondBordersDependents
from authentication.models import CountryDialCodes,CustomUser
from datetime import datetime
from django.forms.models import model_to_dict 
from django.db import IntegrityError
import os
import logging
import base64



# log configuration
logging.basicConfig(
    format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='[%d/%b/%Y %H:%M:%S]')




@login_required(login_url='auth/signin')
def add_dependents(request):
    return render(request, 'nhcp_registration.html')



@login_required(login_url='auth/signin')
def add_dependents_test(request):
    logged_in_user = request.user
    custom_user_obj = CustomUser.objects.get(email = logged_in_user)
    print('custom_user_obj.gender: ',custom_user_obj.gender)
    print('custom_user_obj.date_of_birth: ',custom_user_obj.date_of_birth)
    print('custom_user_obj.foreign_address: ',custom_user_obj.foreign_address)
    if custom_user_obj.gender and custom_user_obj.date_of_birth and custom_user_obj.foreign_address:
        print('in custom_user_obj.gender and custom_user_obj.date_of_birth and custom_user_obj.foreign_address')
        context = {'user_details_already_submitted':'successs'}
        print('context: ',context)
        # return render(request, 'nhcp_registration_test.html',{'dependent_saved':'successs'})
        return render(request, 'beyond_borders/nhcp_registration_test.html',{'context':context})
    else:
        print('in else of custom_user_obj.gender and custom_user_obj.date_of_birth and custom_user_obj.foreign_address')
        return render(request, 'beyond_borders/nhcp_registration_test.html')



@login_required(login_url='auth/signin')
def save_dependent(request):
    # print('request.data: ',request.data)
    print("POST data:")
    # for key, value in request.POST.items():
    #     print(f"{key}: {value}")
    if request.method == 'POST':
        print('in post')
        date_of_birth = None
        gender = None
        foreign_address = None
        if request.POST.get('datepicker-date'):
            date_of_birth = request.POST.get('datepicker-date')
            print('date_of_birth ',date_of_birth)
        if request.POST.get('user_gender'):
            gender = request.POST.get('user_gender')
            print('gender ',gender)
        if request.POST.get('foreign_address'):
            foreign_address = request.POST.get('foreign_address')
            print('foreign_address ',foreign_address)
        print('date_of_birth: ',date_of_birth)
        if date_of_birth or gender or foreign_address:
            logging.info(f'Adding User {request.user} Date Of Birth, Gender and Foreign Address')
            user_obj = CustomUser.objects.get(email = request.user)
            if date_of_birth:
                try:
                    # Step 1: Parse the date string from DD-MM-YYYY format
                    date_of_birth = datetime.strptime(date_of_birth, '%d-%m-%Y')
                    print('dependent_dob_date: ',date_of_birth)
                    # Step 2: Format the date to YYYY-MM-DD format (Django's default format for DateField)
                    formatted_date_of_birth = date_of_birth.strftime('%Y-%m-%d')
                    print('formatted_dependent_dob: ',formatted_date_of_birth)
                    user_obj.date_of_birth = formatted_date_of_birth
                except Exception as e:
                    logging.error('e: ',e)
                    return render(request, 'nhcp_registration_test.html',{'error':"Something Went Wrong, Try Again"})
            if gender:
                user_obj.gender = gender
            if gender:
                user_obj.foreign_address = foreign_address
            try:
                logging.info("saving user gender,dob, address")
                user_obj.save()
                logging.info("user gender,dob, address saved")
            except Exception as e:
                    print('e: ',e)
                    logging.error("can't save User")
                    return render(request, 'beyond_borders/nhcp_registration_test.html',{'error':"Something Went Wrong, Try Again"})
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        dependent_dob = request.POST.get('dependent_datepicker-date')
        dependent_gender = request.POST.get('dependent_gender')
        dependent_relation = request.POST.get('relation')
        phone_number_with_country_code = request.POST.get('mobile-number')
        country = request.POST.get('country')
        dependent_address = request.POST.get('dependent_address')
        current_issue_treatment_expected = request.POST.get('current_issue_treatment_expected')
        health_insurance_details = request.POST.get('health_insurance_details')
        dependent_doc = request.FILES.get('dependent_doc')
        print("firstname: ",first_name)
        print("lastname: ",last_name)
        print("email: ",email)
        # beyond_borders_obj = BeyondBordersDependents( first_name = first_name, last_name = last_name, email = email, date_of_birth = dependent_dob, gender = dependent_gender, relation = dependent_relation, phone_number = phone_number, 
        #                                               country = , address = dependent_address, current_issue_treatment_expected = current_issue_treatment_expected, health_insurance_details = health_insurance_details )
        try:
            dependent_country_code, dependent_phone_number = phone_number_with_country_code.split(' ') 
            print('dependent_country_code: ',dependent_country_code)
            print('dependent_phone_number: ',dependent_phone_number)
            # dependent_country = CountryDialCodes.objects.get(country_dial_code = dependent_country_code)
            dependent_country = CountryDialCodes.objects.get(country_name = country)
            print('dependent_country: ',dependent_country)
            if dependent_dob:
                try:
                    # Step 1: Parse the date string from DD-MM-YYYY format
                    dependent_dob_date = datetime.strptime(dependent_dob, '%d-%m-%Y')
                    print('dependent_dob_date: ',dependent_dob_date)
                    # Step 2: Format the date to YYYY-MM-DD format (Django's default format for DateField)
                    formatted_dependent_dob = dependent_dob_date.strftime('%Y-%m-%d')
                    print('formatted_dependent_dob: ',formatted_dependent_dob)
                except Exception as e:
                    print('e: ',e)
                    logging.error("Can't Format the Dependent Date of Birth")
                    return render(request, 'nhcp_registration_test.html',{'error':"Something Went Wrong, Try Again"})
            try:
                reffered_by_user = CustomUser.objects.get(email = request.user)
                print('reffered_by_user: ',reffered_by_user)
                new_filename = ""
                if dependent_doc:
                        # Handle file processing
                        print(f"Received file: {dependent_doc.name}")
                        # Extract original file extension
                        file_extension = os.path.splitext(dependent_doc.name)[1]
                        # Generate a new filename (e.g., based on current timestamp)
                        new_filename = f"{request.user}-{email}-{datetime.now().strftime('%Y%m%d%H%M%S')}{file_extension}"
                        timenow = datetime.strptime(datetime.now().strftime('%Y%m%d%H%M%S'), '%Y%m%d%H%M%S')
                        # Format the datetime object into a more readable string format
                        readable_format = timenow.strftime('%Y-%m-%d %H:%M:%S')
                        print('Readable Format:', readable_format)
                        save_path = os.path.join(SETTINGS.BASE_DIR, 'static', 'assets', 'img', 'beyond_border_dependents_doc', new_filename)
                        try:
                            # Writing the uploaded file to the specified directory
                            with open(save_path, 'wb+') as destination:
                                for chunk in dependent_doc.chunks():
                                    destination.write(chunk)
                        except Exception as e:
                            # Handle exceptions that occurred during file upload
                            print(f"Failed to upload file. Error: {e}")
                            # return HttpResponse("Failed to upload file.", status=500)
                try:
                    logging.info("Creating beyond borders dependent object")
                    beyond_borders_dependent_obj = BeyondBordersDependents( refered_by = reffered_by_user, first_name = first_name, last_name = last_name, email = email, date_of_birth = formatted_dependent_dob,
                                                                            gender = dependent_gender, relation = dependent_relation, phone_number = dependent_phone_number, 
                                                                            address = dependent_address, current_issue_treatment_expected = current_issue_treatment_expected, 
                                                                            country = dependent_country, health_insurance_details = health_insurance_details, image_filename = new_filename )
                    logging.info("Saving beyond borders dependent object")
                    dependent_saved = beyond_borders_dependent_obj.save()
                    print("dependent_saved: ",dependent_saved)
                    if request.POST.get('finished') == 'on':
                        return redirect('/view_dependents')
                        # return render(request, 'nhcp_registration_test.html',{'error':"Something Went Wrong, Try Again"})
                    else:
                        context = {
                            'dependent_saved':'successs',
                            'user_details_already_submitted':'successs'
                        }
                        print('context: ',context)
                        return render(request, 'beyond_borders/nhcp_registration_test.html',{'context':context})
                except IntegrityError as e:
                    if 'UNIQUE constraint failed' in str(e):
                        print(f"Error: A record with the email '{email}' already exists.")
                    return render(request, 'beyond_borders/nhcp_registration_test.html',{'error':"Email already exists, Try Again"})
                except Exception as e:
                    print('e: ',e)
                    logging.error("")
                    return render(request, 'beyond_borders/nhcp_registration_test.html',{'error':"Something Went Wrong, Try Again"})
            except Exception as e:
                print('e: ',e)
                logging.error("Can't get Reffered User Object")
                return render(request, 'beyond_borders/nhcp_registration_test.html',{'error':"Something Went Wrong, Try Again"})
        except Exception as e:
            print('e: ',e)
            logging.error("Can't get Country details for Phone Number")
            return render(request, 'beyond_borders/nhcp_registration_test.html',{'error':"Something Went Wrong, Try Again"})
    else:
        logged_in_user = request.user
        custom_user_obj = CustomUser.objects.get(email = logged_in_user)
        if custom_user_obj.gender and custom_user_obj.date_of_birth and custom_user_obj.foreign_address:
            print('in custom_user_obj.gender and custom_user_obj.date_of_birth and custom_user_obj.foreign_address')
            context = {'user_details_already_submitted':'successs'}
            print('context: ',context)
            # return render(request, 'nhcp_registration_test.html',{'dependent_saved':'successs'})
            return render(request, 'beyond_borders/nhcp_registration_test.html',{'context':context})
        else:
            print('in else of custom_user_obj.gender and custom_user_obj.date_of_birth and custom_user_obj.foreign_address')
            return render(request, 'beyond_borders/nhcp_registration_test.html')



@login_required(login_url='auth/signin')
def view_dependents(request):
    logged_in_user = request.user
    print('logged_in_user: ', logged_in_user)
    user_dependents = BeyondBordersDependents.objects.filter(refered_by=logged_in_user)

    # Initialize an empty list to hold dependents' details
    dependents_list = []

    # Iterate through user_dependents queryset
    for dependent in user_dependents:
        print('dependent: ', dependent.country)
        # Convert each dependent object to a dictionary
        dependent_dict = model_to_dict(dependent)
        print(dependent_dict)  

        dependent_dict['country'] = dependent.country.country_name
        
        dependents_list.append(dependent_dict)
        

    return render(request, 'beyond_borders/view_dependents.html', {'dependents_list': dependents_list})



@login_required(login_url='auth/signin')
def view_dependent(request,dep_id):
    print('dep_id: ',dep_id)
    dependent = BeyondBordersDependents.objects.get(membership_id = dep_id)
    dependent_dict = model_to_dict(dependent)
    print(dependent_dict)  
    dependent_dict['country'] = dependent.country.country_name

    # Retrieve the image filename from the dependent details
    image_filename = dependent_dict.get('image_filename')  # Replace 'image_field_name_here' with the actual name of the image field in your model
    print('image_filename: ',image_filename)
    if image_filename != '':
        print('image_filename is None')
        # Construct the image path
        image_path = os.path.join(SETTINGS.BASE_DIR, 'static', 'assets', 'img', 'beyond_border_dependents_doc', image_filename)

        # Check if the image file exists
        if os.path.exists(image_path):
            # Read the image file
            with open(image_path, 'rb') as image_file:
                # Encode the image data to Base64
                image_data = base64.b64encode(image_file.read()).decode('utf-8')  # Decode bytes to UTF-8 string
        else:
            # If the image file does not exist, set image_data to None or handle the case accordingly
            image_data = None
    else:
        image_data = None

    # Add the image data to the dependent dictionary
    dependent_dict['image_data'] = image_data
    return render(request, 'beyond_borders/view_dependent.html', {'dependent_dict': dependent_dict})




