from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import event_view
from api.views import category_view
from django.contrib import admin
 
urlpatterns = [ 
    path('events/', event_view.EventList.as_view()),
    path('events/<slug:pk>/', event_view.EventDetail.as_view()),

    # Events by user
    path('events/user_registered/<slug:userId>/', event_view.UserEventList.as_view()),
    path('events/user_not_registered/<slug:userId>/', event_view.UserNoEventList.as_view()),


    # Categories
    path('category/', category_view.CategoryList.as_view()),
    path('category/<slug:pk>/', category_view.CategoryDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
