from django.urls import path
from .views import News_view, New_detail

urlpatterns=[
    path('', News_view.as_view() ,name='home'),
    path('news/<int:pk>', New_detail.as_view(), name='detail')
]