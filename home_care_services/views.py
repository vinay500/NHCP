from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRegistrations, Services
from authentication.models import CustomUser, CountryDialCodes
from django.forms.models import model_to_dict 


# Create your views here.
@login_required(login_url='auth/signin')
def home_care_services(request):
    return render(request, 'home_care_services/home_care_services.html')



@login_required(login_url='/auth/signin')
def book_home_care_service(request, service_name):
    print("in book_home_care_service")
    # print("------------------------------ service name: ", service_name, "-------------------------------")
    context = {"service_name": service_name}
    # print("context: ",context)
    if request.method == "POST":
        for key, value in request.POST.items():
                print(f"{key}: {value}")
        custom_user_obj = CustomUser.objects.get(email = request.user)
        service_register_obj = ServiceRegistrations()
        service_register_obj.user = custom_user_obj
        service = Services.objects.get(service_name = request.POST.get('service'))
        service_register_obj.service = service
        country = CountryDialCodes.objects.get(country_name = request.POST.get('country'))
        service_register_obj.country = country
        service_register_obj.name = request.POST.get('name')
        service_register_obj.email = request.POST.get('email')
        print("mobile_number: ",request.POST.get('mobile-number').split(" ")[1])
        service_register_obj.mobile_number = request.POST.get('mobile-number').split(" ")[1]
        service_register_obj.gender = request.POST.get('gender')
        service_register_obj.pin_code = request.POST.get('pincode')
        service_register_obj.city = request.POST.get('city')
        service_register_obj.state = request.POST.get('state')
        service_booking_saved = service_register_obj.save()
        print("service_booking_saved: ",service_booking_saved)
        # return HttpResponse("<p>user saved successfully</p>")
        return redirect('booked_services')
    else:
        return render(request, 'home_care_services/book_home_care_service.html',context)
    


@login_required(login_url='auth/signin')
def view_booked_services(request):
    services_booked = ServiceRegistrations.objects.filter(user=request.user).order_by('-created_at')

    # Initialize an empty list to hold dependents' details
    services_booked_list = []
    for service in services_booked:
        service_dict = model_to_dict(service)
        print(service_dict)  
        service_dict['country'] = service.country.country_name
        service_dict['service'] = service.service.service_name
        # Manually add the created_at field because model_to_dict() 
        # does not include fields with auto_now_add because auto_now_add attribute is not editable 
        service_dict['created_at'] = service.created_at 
        print("service_dict['created_at']: ",service_dict['created_at']) 
        print(service_dict) 
        services_booked_list.append(service_dict)

    return render(request, 'home_care_services/view_booked_services.html', {'services_list': services_booked_list})
     