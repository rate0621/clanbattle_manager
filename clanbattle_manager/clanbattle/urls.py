from django.urls import path
from . import views

app_name = 'clanbattle'
urlpatterns = [
    path('', views.CbListView.as_view(), name='index'),
    path('popup/update_target/<int:pk>', views.TargetUpdateView.as_view(), name='popup_update_target'),
    path('update_damage/<int:pk>', views.DamageUpdateView.as_view(), name='update_damage'),
]
