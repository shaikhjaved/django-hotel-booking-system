from django.urls import path

from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.index, name='index'),
    path('onGetCreate/', views.onGetCreate, name='onGetCreate'),
    path('onPostCreate/', views.onPostCreate, name='onPostCreate'),
    path('<int:id>', views.onGetEdit, name='onGetEdit'),
    path('onPostEdit/<int:id>', views.onPostEdit, name='onPostEdit'),
    path('onPostDelete/<int:id>', views.onPostDelete, name='onPostDelete'),
]