from nz.views import *
from django.urls import path

app_name='anything'

urlpatterns=[
    path('phillips/',phillips,name='phillips'),
    path('williamson/',williamson,name='williamson'),
]