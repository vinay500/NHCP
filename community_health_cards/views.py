from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import logging
import base64



# log configuration
logging.basicConfig(
    format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='[%d/%b/%Y %H:%M:%S]')
# examples
# logging.info("Log Info Message")
# logging.warning("Log Warning Message")
# logging.error("Log Error Message")



# Create your views here.
@login_required(login_url='auth/signin')
def buy_health_card(request):
    return render(request, 'buy_health_card.html')



@login_required(login_url='auth/signin')
def assign_membership_card(request):
    if request.method == 'POST':
        logging.info("In assign_membership_card post request")
        # print('request.data: ',request.post.data)
        # print("POST data:")
        for key, value in request.POST.items():
            print(f"{key}: {value}")
        return HttpResponse("assign_membership_card post data")
    else:
        logging.info("In assign_membership_card get request")
        return HttpResponse("assign_membership_card get data")