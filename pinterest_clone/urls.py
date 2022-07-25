
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('home/' , views.home , name='home'),
    path('SignUp/' , views.handleSignUp),
    path('Login/' , views.handleLogin),

    path('Logout/' , views.handleLogout),
    path('ReachUs/' , views.ReachUs),
    path('feedback/' , views.feedback),
    path('Profile/' , views.profile),
    path('Liked/' , views.liked),
    path('Saved/' , views.saved),
    path('Uploaded/' , views.uploaded),

    path('image_view/<int:id>/' , views.image_view , name='image_view'),
    path('liking/<int:id>/' , views.liking),
    path('saving/<int:id>/' , views.saving),

    path('upload_page/' , views.upload_page),
    path('uploading/' , views.uploading),

    path('Settings/' , views.Settings, name='Settings'),
    path('update_profile/' , views.update_profile),
    path('change_password/' , views.change_password),
    
    path('interest/' , views.interest),

    path('home/searching/<str:category>/' , views.home_searching),
    path('Liked/searching/<str:category>/' , views.liked_searching),
    path('Saved/searching/<str:category>/' , views.saved_searching),
    path('Uploaded/searching/<str:category>/' , views.uploaded_searching),

    path('profile/<str:username>/' , views.user_profile),

    path('admin/', admin.site.urls),
    path('accounts/' , include('allauth.urls')),

    path('reset_password/' , auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/' , auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/' , auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
