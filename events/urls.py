from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
from events import views 
from django.contrib import admin
 
urlpatterns = [ 
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)