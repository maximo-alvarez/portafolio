from django.urls import path, include
from django.contrib.auth import views as auth_views

from app.seguridad import views

urlpatterns = [
    path("", views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('mensaje/crear', views.mensaje_crear, name='mensaje_crear'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("curriculum", views.CurriculumIndexAdmin.as_view(), name='curriculum'),
    path("<str:username>", views.CurriculumIndex.as_view(), name='curriculum_index'),
]
