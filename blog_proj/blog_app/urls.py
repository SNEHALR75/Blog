from django.urls import path
from .import views



urlpatterns = [
    path('add/',views.add_view),
    path('show/',views.show_view),
    path('update/<i>',views.update_view),
    path('delete/<i>',views.delete_view),
    path('register/',views.register_view),
    path('login/',views.login_view),
    path('logout/',views.logout_view),
]