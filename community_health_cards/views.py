from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from community_health_cards.models import MembershipCard
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
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


@login_required(login_url='auth/signin')
def view_health_cards(request):
    return render(request, 'community_health_cards/community_health_cards.html')
    # return render(request, 'components/base.html')


@login_required(login_url='/auth/signin')
# @permission_required('community_health_cards.add_membershipcard', raise_exception=True)
def buy_health_card(request, card_type):
    context = {}
    
    print("card_type:",card_type)
    if card_type == "basic":
        context['health_card_img'] = r"assets\img\nhcp_imgs\nhcp_programs\current_basic_membership_card.png"
        # get membership plan benefits
        memberhip_card_obj = MembershipCard.objects.get(type = 'Basic')
        print("memberhip_card_obj: ",memberhip_card_obj)
        context['membership_card'] = memberhip_card_obj
    if card_type == "essential":
        context['health_card_img'] = r'assets\img\nhcp_imgs\nhcp_programs\current_essential_membership_card.png'
        # get membership plan benefits
        memberhip_card_obj = MembershipCard.objects.get(type = 'Essential')
        print("memberhip_card_obj: ",memberhip_card_obj)
        context['membership_card'] = memberhip_card_obj

    return render(request, 'community_health_cards/buy_health_card.html', context)



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
    


@login_required(login_url='auth/signin')
def assign_health_card_role(request):
    group = Group.objects.get(name='Health Cards Admin')
    request.user.groups.add(group)