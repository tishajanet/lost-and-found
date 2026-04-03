from django.contrib import admin
from django.urls import path
from items import views
from django.contrib.auth import views as auth_vie
from django.contrib.auth import views as auth_views
path('logout/', auth_views.LogoutView.as_view(), name='logout'),

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.item_list),

    # Item
    path('item/<int:item_id>/', views.item_detail),
    path('item/<int:item_id>/claim/', views.claim_item),

    # Report
    path('report-item/', views.report_item),

    # AUTH
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('my-claims/', views.my_claims),

    path('all-claims/', views.all_claims),
]