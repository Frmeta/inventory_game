from django.urls import path
from main.views import create_product_flutter, show_main, create_item, show_xml, show_json, show_json_by_id, show_xml_by_id
from main.views import register, login_user, logout_user, add, remove, remove_all
from main.views import get_item_json, create_ajax, add_ajax, remove_ajax, remove_all_ajax
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add/<int:id>/', add, name='add'),
    path('remove/<int:id>/', remove, name='remove'),
    path('remove-all/<int:id>/', remove_all, name='remove_all'),

    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('add-ajax/', add_ajax, name='add_ajax'),
    path('remove-ajax/', remove_ajax, name='remove_ajax'),
    path('remove-all-ajax/', remove_all_ajax, name='remove_all_ajax'),

    # Flutter
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),

]