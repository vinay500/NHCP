from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser
from .models import Program, UsersRegistered
from django.http import HttpResponse
from django.conf import settings as SETTINGS
from django.http import JsonResponse
import logging
import os

# log configuration
logging.basicConfig(
    format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='[%d/%b/%Y %H:%M:%S]')
# examples
# logging.info("Log Info Message")
# logging.warning("Log Warning Message")
# logging.error("Log Error Message")


@login_required(login_url='/auth/signin')
def index(request):
    print('in index view')
    logged_in_user = request.user
    print('logged in user: ',logged_in_user)
    user_register_programs = UsersRegistered.objects.filter(user = logged_in_user)
    print('user_register_programs: ',user_register_programs)
    if len(user_register_programs) > 0:
        # programs_registered = {
        #     'beyond_borders':False,
        #     'community_health_cards':False,
        #     'heal_in_india':False,
        #     'home_care_services':False
        #     }
        # for registered_program in user_register_programs:
        #     print('program: ',registered_program)
        #     print('program name: ',registered_program.program)
        #     if registered_program.program == 'Beyond Borders':
        #         programs_registered['beyond_borders'] = True
        #     if registered_program.program == 'Community Health Cards':
        #         programs_registered['community_health_cards'] = True
        #     if registered_program.program == 'Heal In India':
        #         programs_registered['heal_in_india'] = True
        #     if registered_program.program == 'Home Care Services':
        #         programs_registered['home_care_services'] = True
        # print('programs_registered: ',programs_registered)
        # return render(request, 'index.html', {'programs_registered': programs_registered})

        programs_registered = []
        for registered_program in user_register_programs:
            print('program: ',registered_program)
            print('program name: ',registered_program.program)
            programs_registered.append(registered_program.program.program_name)
        print('programs_registered: ',programs_registered)
        print('Beyond Borders in programs_registered: ', 'Beyond Borders' in programs_registered)
        return render(request, 'index.html', {'programs_registered': programs_registered})
    else:
        return render(request, 'index.html')
    


@login_required(login_url='/auth/signin')
def get_user_programs(request):
    print('in index view')
    logged_in_user = request.user
    print('logged in user: ',logged_in_user)
    user_register_programs = UsersRegistered.objects.filter(user = logged_in_user)
    print('user_register_programs: ',user_register_programs)
    if len(user_register_programs) > 0:
        programs_registered = []
        for registered_program in user_register_programs:
            print('program: ',registered_program)
            print('program name: ',registered_program.program)
            programs_registered.append(registered_program.program.program_name)
        print('programs_registered: ',programs_registered)
        print('Beyond Borders in programs_registered: ', 'Beyond Borders' in programs_registered)
        return JsonResponse({'programs_registered':programs_registered})
    else:
        return JsonResponse({'programs_registered':[]})



@login_required(login_url='/auth/signin')
def register_user_for_program(request, program_url_param):
    print("program_url_param", program_url_param)
    print('in register_user_for_program')
    user = request.user
    print('current user:', user)
    logging.info("Logged In User: %s", user)
    
    if request.method == 'POST':
        print('in post method')
        program = request.POST.get('program_name')
        logging.info("User trying to Register for the Program: %s", program)
        print('program: ', program)
        
        try:
            user_obj = CustomUser.objects.get(email=user.email)
            program_obj = Program.objects.get(program_name=program)
            print('user_obj: ', user_obj)
            print('program_obj: ', program_obj)
            
            if UsersRegistered.objects.filter(program=program_obj, user=user_obj).exists():
                logging.info('User Already Registered in the Program')
                if program_url_param == "beyond_borders":
                    return redirect('add_dependents_test')
                elif program_url_param == "community_health_cards":
                    return redirect('view_health_cards')
                elif program_url_param == "home_care_services":
                    return redirect('home_care_services')
                else:
                    return render(request, 'index.html', {'error': 'Unknown program'})
            else:
                user_register_obj = UsersRegistered(program=program_obj, user=user_obj)
                try:
                    user_register_obj.save()
                    print('user_register_obj saved')
                    logging.info(f"User {user} Registered for the Program: {program}")
                    if program_url_param == "beyond_borders":
                        return redirect('add_dependents_test')
                    elif program_url_param == "community_health_cards":
                        return redirect('view_health_cards')
                    elif program_url_param == "home_care_services":
                        return redirect('home_care_services')
                    else:
                        return render(request, 'index.html', {'error': 'Unknown program'})
                except Exception as e:
                    logging.error("Can't Register User for the Program: %s", e)
                    print('e: ', e)
                    return render(request, 'index.html', {'error': 'Unable to Register, Try Again'})
        except Exception as e:
            logging.error("Can't Register User for the Program: %s", e)
            print('e: ', e)
            return render(request, 'index.html', {'error': 'Unable to Register, Try Again'})
    else:
        return HttpResponse("<h1>not post request</h1>")


    

# Create your views here.
def aboutus(request):
    return render(request, 'aboutus.html')
def accordion(request):
    return render(request, 'accordion.html')
def alerts(request):
    return render(request, 'alerts.html')
def avatar(request):
    return render(request, 'avatar.html')
def background(request):
    return render(request, 'background.html')
def badge(request):
    return render(request, 'badge.html')
def blog_details(request):
    return render(request, 'blog-details.html')
def blog(request):
    return render(request, 'blog.html')
def border(request):
    return render(request, 'border.html')
def breadcrumbs(request):
    return render(request, 'breadcrumbs.html')
def buttons(request):
    return render(request, 'buttons.html')
def calendar(request):
    return render(request, 'calendar.html')
def cards(request):
    return render(request, 'cards.html')
def carousel(request):
    return render(request, 'carousel.html')
def chart_chartjs(request):
    return render(request, 'chart-chartjs.html')
def chart_echart(request):
    return render(request, 'chart-echart.html')
def chart_flot(request):
    return render(request, 'chart-flot.html')
def chart_morris(request):
    return render(request, 'chart-morris.html')
def chart_peity(request):
    return render(request, 'chart-peity.html')
def chart_sparkline(request):
    return render(request, 'chart-sparkline.html')
def chat(request):
    return render(request, 'chat.html')
def check_out(request):
    return render(request, 'check-out.html')
def collapse(request):
    return render(request, 'collapse.html')
def contacts(request):
    return render(request, 'contacts.html')
def counters(request):
    return render(request, 'counters.html')
def display(request):
    return render(request, 'display.html')
def draggablecards(request):
    return render(request, 'draggablecards.html')
def dropdown(request):
    return render(request, 'dropdown.html')
def edit_post(request):
    return render(request, 'edit-post.html')
def emptypage(request):
    return render(request, 'emptypage.html')
def error404(request):
    return render(request, 'error404.html')
def error500(request):
    return render(request, 'error500.html')
def error501(request):
    return render(request, 'error501.html')
def extras(request):
    return render(request, 'extras.html')
def faq(request):
    return render(request, 'faq.html')
def file_attached_tags(request):
    return render(request, 'file-attached-tags.html')
def file_details(request):
    return render(request, 'file-details.html')
def file_manager(request):
    return render(request, 'file-manager.html')
def file_manager1(request):
    return render(request, 'file-manager1.html')
def flex(request):
    return render(request, 'flex.html')
def forgot(request):
    return render(request, 'forgot.html')
def form_advanced(request):
    return render(request, 'form-advanced.html')
def form_editor(request):
    return render(request, 'form-editor.html')
def form_elements(request):
    return render(request, 'form-elements.html')
def form_layouts(request):
    return render(request, 'form-layouts.html')
def form_sizes(request):
    return render(request, 'form-sizes.html')
def form_validation(request):
    return render(request, 'form-validation.html')
def form_wizards(request):
    return render(request, 'form-wizards.html')
def gallery(request):
    return render(request, 'gallery.html')
def height(request):
    return render(request, 'height.html')
def icons(request):
    return render(request, 'icons.html')
def icons2(request):
    return render(request, 'icons2.html')
def icons3(request):
    return render(request, 'icons3.html')
def icons4(request):
    return render(request, 'icons4.html')
def icons5(request):
    return render(request, 'icons5.html')
def icons6(request):
    return render(request, 'icons6.html')
def icons7(request):
    return render(request, 'icons7.html')
def icons8(request):
    return render(request, 'icons8.html')
def icons9(request):
    return render(request, 'icons9.html')
def icons10(request):
    return render(request, 'icons10.html')
def icons11(request):
    return render(request, 'icons11.html')
def icons12(request):
    return render(request, 'icons12.html')
def image_compare(request):
    return render(request, 'image-compare.html')
def images(request):
    return render(request, 'images.html')



def index1(request):
    return render(request, 'index1.html')
def index2(request):
    return render(request, 'index2.html')
def invoice(request):
    return render(request, 'invoice.html')
def list_group(request):
    return render(request, 'list-group.html')
def lockscreen(request):
    return render(request, 'lockscreen.html')
def mail_compose(request):
    return render(request, 'mail-compose.html')
def mail_read(request):
    return render(request, 'mail-read.html')
def mail_settings(request):
    return render(request, 'mail-settings.html')
def mail(request):
    return render(request, 'mail.html')
def map_leaflet(request):
    return render(request, 'map-leaflet.html')
def map_vector(request):
    return render(request, 'map-vector.html')
def margin(request):
    return render(request, 'margin.html')
def media_object(request):
    return render(request, 'media-object.html')
def modals(request):
    return render(request, 'modals.html')
def navigation(request):
    return render(request, 'navigation.html')
def notification(request):
    return render(request, 'notification.html')
def padding(request):
    return render(request, 'padding.html')
def pagination(request):
    return render(request, 'pagination.html')
def popover(request):
    return render(request, 'popover.html')
def position(request):
    return render(request, 'position.html')
def pricing(request):
    return render(request, 'pricing.html')
def product_cart(request):
    return render(request, 'product-cart.html')
def product_details(request):
    return render(request, 'product-details.html')
def profile_notifications(request):
    return render(request, 'profile-notifications.html')
def profile(request):
    return render(request, 'profile.html')
def progress(request):
    return render(request, 'progress.html')
def rangeslider(request):
    return render(request, 'rangeslider.html')
def rating(request):
    return render(request, 'rating.html')
def reset(request):
    return render(request, 'reset.html')
def search(request):
    return render(request, 'search.html')
def settings(request):
    return render(request, 'settings.html')
def shop(request):
    return render(request, 'shop.html')

def spinners(request):
    return render(request, 'spinners.html')
def sweet_alert(request):
    return render(request, 'sweet-alert.html')
def switcherpage(request):
    return render(request, 'switcherpage.html')
def table_basic(request):
    return render(request, 'table-basic.html')
def table_data(request):
    return render(request, 'table-data.html')
def tabs(request):
    return render(request, 'tabs.html')
def tags(request):
    return render(request, 'tags.html')
def thumbnails(request):
    return render(request, 'thumbnails.html')
def timeline(request):
    return render(request, 'timeline.html')
def toast(request):
    return render(request, 'toast.html')
def todotask(request):
    return render(request, 'todotask.html')
def tooltip(request):
    return render(request, 'tooltip.html')
def treeview(request):
    return render(request, 'treeview.html')
def typography(request):
    return render(request, 'typography.html')
def underconstruction(request):
    return render(request, 'underconstruction.html')
def userlist(request):
    return render(request, 'userlist.html')
def widget_notification(request):
    return render(request, 'widget-notification.html')
def widgets(request):
    return render(request, 'widgets.html')
def width(request):
    return render(request, 'width.html')
def wish_list(request):
    return render(request, 'wish-list.html')