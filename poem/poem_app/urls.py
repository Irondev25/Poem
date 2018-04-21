from django.urls import path
from . import views

app_name = 'poem'

urlpatterns = [
    path('/', views.PoemList.as_view(), name='list'),
    path('<slug:slug>/', views.PoemDetail.as_view(), name='detail'),
    path('poem/create/', views.PoemCreate.as_view(), name='create'),
    path('<slug:slug>/update/', views.PoemUpdate.as_view(), name='update'),
    path('<slug:slug>/delete', views.PoemDelete.as_view(), name='delete'),
]
