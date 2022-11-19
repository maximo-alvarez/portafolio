from django.urls import path, include
from django.contrib.auth import views as auth_views

from seguridad import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('mensaje/crear', views.mensaje_crear, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("", views.home, name='home'),
    path("curriculum", views.Curriculum.as_view(), name='curriculum'),
    path("curriculum2", views.CurriculumIndex.as_view(), name='curriculum_index'),
]
