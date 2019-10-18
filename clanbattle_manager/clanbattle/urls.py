from django.urls import path
from . import views

app_name = 'clanbattle'
urlpatterns = [
    path('', views.BossListView.as_view(), name='index'),
    path('popup/update_target/<int:pk>', views.TargetUpdateView.as_view(), name='popup_update_target'),
]
