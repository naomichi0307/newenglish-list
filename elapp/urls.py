from django.urls import path
from .views import englishlist, englishdetail, englishcreate, englishdelete, englishupdate, Englishlist_danger, Englishlist_info, Englishlist_success
from . import views

urlpatterns = [
    path('list/', englishlist.as_view(), name = 'list'),
    path('detail/<int:pk>', englishdetail.as_view(), name='detail'),
    path('create/', englishcreate.as_view(), name='create'),
    path('delete/<int:pk>', englishdelete.as_view(), name='delete'),
    path('update/<int:pk>', englishupdate.as_view(), name='update'),
    path('form/', views.add_venue, name='form'),
    path('list/danger', Englishlist_danger.as_view(), name='list_danger'),
    path('list/info', Englishlist_info.as_view(), name='list_info'),
    path('list/success', Englishlist_success.as_view(), name='list_success')
]
