from django.urls import path
from .views import englishlist, englishdetail, englishcreate, englishdelete, englishupdate
from . import views

urlpatterns = [
    path('list/', englishlist.as_view(), name = 'list'),
    path('detail/<int:pk>', englishdetail.as_view(), name='detail'),
    path('create/', englishcreate.as_view(), name='create'),
    path('delete/<int:pk>', englishdelete.as_view(), name='delete'),
    path('update/<int:pk>', englishupdate.as_view(), name='update'),
    path('form/', views.add_venue, name='form')
]
