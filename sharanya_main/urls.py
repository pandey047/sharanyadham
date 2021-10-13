from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('event', views.event, name='event'),
    path('about-us', views.aboutus, name='aboutus'),
    path('contact-us', views.contactus, name='contactus'),
    path('gallery', views.gallery, name='gallery'),
    path('pooja', views.pooja, name='pooja'),


    path('ved', views.ved, name='ved'),
    path('puran', views.puran, name='puran'),
    path('upnishads', views.upnishads, name='upnishads'),
    path('geeta', views.geeta, name='geeta'),
    path('ramcharitmanas', views.ramcharitmanas, name='ramcharitmanas'),
    path('god', views.god, name='god'),
    path('goddess', views.goddess, name='goddess'),
    path('naugrah', views.naugrah, name='naugrah'),
    path('final_design',views.final_design,name='final_design'),
    path('bhoomi_poojan',views.bhoomi_poojan,name='bhoomi_poojan'),
    path('stage10',views.stage10,name='stage10'),
    path('stage9',views.stage9,name='stage9'),
    path('stage8',views.stage8,name='stage8'),
    path('stage7',views.stage7,name='stage7'),
    path('stage6',views.stage6,name='stage6'),
    path('stage5',views.stage5,name='stage5'),
    path('stage4',views.stage4,name='stage4'),
    path('stage3',views.stage3,name='stage3'),
    path('stage2',views.stage2,name='stage2'),
    path('stage1',views.stage1,name='stage1'),
    path('thank_you',views.thank_you,name='thank_you'),
    path('aarti',views.aarti,name='aarti'),
    path('chalisa',views.chalisa,name='chalisa'),
    path('mantra',views.mantra,name='mantra'),
    path('aart-ganeshji',views.aarti_ganeshji,name='aarti-ganeshji'),
    path('aart-krishnaji',views.aarti_krishnaji,name='aarti-krishnaji'),
    path('aart-laxmiji',views.aarti_laxmiji,name='aarti-laxmiji'),
    path('aart-shanidevji',views.aarti_shanidevji,name='aarti-shanidevji'),
    path('aart-ramayanji',views.aarti_ramayanji,name='aarti-ramayanji'),
    path('aart-durgaji',views.aarti_durgaji,name='aarti-durgaji'),
    path('aart-ramji',views.aarti_ramji,name='aarti-ramji'),
    path('aart-vishnuji',views.aarti_vishnuji,name='aarti-vishnuji'),
    path('aart-saraswatiji',views.aarti_saraswatiji,name='aarti-saraswatiji'),
    path('aart-hanumanji',views.aarti_hanumanji,name='aarti-hanumanji'),
    path('aart-shivji',views.aarti_shivji,name='aarti-shivji'),
    path('aart-kaliji',views.aarti_kaliji,name='aarti-kaliji'),

    
    
]