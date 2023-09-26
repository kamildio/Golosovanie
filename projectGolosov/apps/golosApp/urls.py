from django.urls import path
from . import views

app_name = 'golosApp'

urlpatterns = [
    path('', views.homePage, name='home'),
    path('candidates/', views.candidatePage, name='candit'),
    path('candidate/form/<int:user_id>/', views.candidateForm, name='canditfr'),
    path('candidate/form/edit/<int:pk>/<int:user_id>/', views.edit_candite_form, name='canditfre'),
    path('candidate/form/new/<int:user_id>/', views.createCandidateForm, name='canditfrn'),
]