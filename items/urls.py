from django.contrib import admin
from django.urls import path
from items import views   # ← this must match your app folder name

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.item_list),
    path('item/<int:item_id>/', views.item_detail),
    path('item/<int:item_id>/claim/', views.claim_item),
    path('report-item/', views.report_item),
    path('register/', views.register, name='register'),
]