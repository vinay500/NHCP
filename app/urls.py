from django.urls import path
from . import views


urlpatterns = [
        # new paths
        path('add_dependents', views.add_dependents , name = 'add_dependents'),
        path('add_dependents_test', views.add_dependents_test , name = 'add_dependents_test'),
        path('save_dependent', views.save_dependent, name = 'save_dependent'),
        # path('reset_password_invalid_token', views.reset_password_invalid_token , name = 'reset_password_invalid_token'),
        
        path('', views.index , name = 'index'),
        path('aboutus', views.aboutus , name = 'aboutus'),
        path('accordion', views.accordion , name = 'accordion'),
        path('alerts', views.alerts , name = 'alerts'),
        path('avatar', views.avatar , name = 'avatar'),
        path('background', views.background , name = 'background'),
        path('badge', views.badge , name = 'badge'),
        path('blog-details', views.blog_details , name = 'blog-details'),
        path('blog', views.blog , name = 'blog'),
        path('border', views.border , name = 'border'),
        path('breadcrumbs', views.breadcrumbs , name = 'breadcrumbs'),
        path('buttons', views.buttons , name = 'buttons'),
        path('calendar', views.calendar , name = 'calendar'),
        path('cards', views.cards , name = 'cards'),
        path('carousel', views.carousel , name = 'carousel'),
        path('chart-chartjs', views.chart_chartjs , name = 'chart-chartjs'),
        path('chart-echart', views.chart_echart , name = 'chart-echart'),
        path('chart-flot', views.chart_flot , name = 'chart-flot'),
        path('chart-morris', views.chart_morris , name = 'chart-morris'),
        path('chart-peity', views.chart_peity , name = 'chart-peity'),
        path('chart-sparkline', views.chart_sparkline , name = 'chart-sparkline'),
        path('chat', views.chat , name = 'chat'),
        path('check-out', views.check_out , name = 'check-out'),
        path('collapse', views.collapse , name = 'collapse'),
        path('contacts', views.contacts , name = 'contacts'),
        path('counters', views.counters , name = 'counters'),
        path('display', views.display , name = 'display'),
        path('draggablecards', views.draggablecards , name = 'draggablecards'),
        path('dropdown', views.dropdown , name = 'dropdown'),
        path('edit-post', views.edit_post , name = 'edit-post'),
        path('emptypage', views.emptypage , name = 'emptypage'),
        path('error404', views.error404 , name = 'error404'),
        path('error500', views.error500 , name = 'error500'),
        path('error501', views.error501 , name = 'error501'),
        path('extras', views.extras , name = 'extras'),
        path('faq', views.faq , name = 'faq'),
        path('file-attached-tags', views.file_attached_tags , name = 'file-attached-tags'),
        path('file-details', views.file_details , name = 'file-details'),
        path('file-manager', views.file_manager , name = 'file-manager'),
        path('file-manager1', views.file_manager1 , name = 'file-manager1'),
        path('flex', views.flex , name = 'flex'),
        
        path('form-advanced', views.form_advanced , name = 'form-advanced'),
        path('form-editor', views.form_editor , name = 'form-editor'),
        path('form-elements', views.form_elements , name = 'form-elements'),
        path('form-layouts', views.form_layouts , name = 'form-layouts'),
        path('form-sizes', views.form_sizes , name = 'form-sizes'),
        path('form-validation', views.form_validation , name = 'form-validation'),
        path('form-wizards', views.form_wizards , name = 'form-wizards'),
        path('gallery', views.gallery , name = 'gallery'),
        path('height', views.height , name = 'height'),
        path('icons', views.icons , name = 'icons'),
        path('icons2', views.icons2 , name = 'icons2'),
        path('icons3', views.icons3 , name = 'icons3'),
        path('icons4', views.icons4 , name = 'icons4'),
        path('icons5', views.icons5 , name = 'icons5'),
        path('icons6', views.icons6 , name = 'icons6'),
        path('icons7', views.icons7 , name = 'icons7'),
        path('icons8', views.icons8 , name = 'icons8'),
        path('icons9', views.icons9 , name = 'icons9'),
        path('icons10', views.icons10 , name = 'icons10'),
        path('icons11', views.icons11 , name = 'icons11'),
        path('icons12', views.icons12 , name = 'icons12'),
        path('image-compare', views.image_compare , name = 'image-compare'),
        path('images', views.images , name = 'images'),
        path('index', views.index , name = 'index'),
        path('index1', views.index1 , name = 'index1'),
        path('index2', views.index2 , name = 'index2'),
        path('invoice', views.invoice , name = 'invoice'),
        path('list-group', views.list_group , name = 'list-group'),
        path('lockscreen', views.lockscreen , name = 'lockscreen'),
        path('mail-compose', views.mail_compose , name = 'mail-compose'),
        path('mail-read', views.mail_read , name = 'mail-read'),
        path('mail-settings', views.mail_settings , name = 'mail-settings'),
        path('mail', views.mail , name = 'mail'),
        path('map-leaflet', views.map_leaflet , name = 'map-leaflet'),
        path('map-vector', views.map_vector , name = 'map-vector'),
        path('margin', views.margin , name = 'margin'),
        path('media-object', views.media_object , name = 'media-object'),
        path('modals', views.modals , name = 'modals'),
        path('navigation', views.navigation , name = 'navigation'),
        path('notification', views.notification , name = 'notification'),
        path('padding', views.padding , name = 'padding'),
        path('pagination', views.pagination , name = 'pagination'),
        path('popover', views.popover , name = 'popover'),
        path('position', views.position , name = 'position'),
        path('pricing', views.pricing , name = 'pricing'),
        path('product-cart', views.product_cart , name = 'product-cart'),
        path('product-details', views.product_details , name = 'product-details'),
        path('profile-notifications', views.profile_notifications , name = 'profile-notifications'),
        path('profile', views.profile , name = 'profile'),
        path('progress', views.progress , name = 'progress'),
        path('rangeslider', views.rangeslider , name = 'rangeslider'),
        path('rating', views.rating , name = 'rating'),
        path('reset', views.reset , name = 'reset'),
        path('search', views.search , name = 'search'),
        path('settings', views.settings , name = 'settings'),
        path('shop', views.shop , name = 'shop'),
        path('spinners', views.spinners , name = 'spinners'),
        path('sweet-alert', views.sweet_alert , name = 'sweet-alert'),
        path('switcherpage', views.switcherpage , name = 'switcherpage'),
        path('table-basic', views.table_basic , name = 'table-basic'),
        path('table-data', views.table_data , name = 'table-data'),
        path('tabs', views.tabs , name = 'tabs'),
        path('tags', views.tags , name = 'tags'),
        path('thumbnails', views.thumbnails , name = 'thumbnails'),
        path('timeline', views.timeline , name = 'timeline'),
        path('toast', views.toast , name = 'toast'),
        path('todotask', views.todotask , name = 'todotask'),
        path('tooltip', views.tooltip , name = 'tooltip'),
        path('treeview', views.treeview , name = 'treeview'),
        path('typography', views.typography , name = 'typography'),
        path('underconstruction', views.underconstruction , name = 'underconstruction'),
        path('userlist', views.userlist , name = 'userlist'),
        path('widget-notification', views.widget_notification , name = 'widget-notification'),
        path('widgets', views.widgets , name = 'widgets'),
        path('width', views.width , name = 'width'),
        path('wish-list', views.wish_list , name = 'wish-list'),
      
]