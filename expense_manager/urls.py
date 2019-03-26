"""expense_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from expenses import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'expenseextract',views.ExpenseViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('expenses', views.ExpenseList.as_view(), name='expense_list'),
    path('expense/<int:pk>', views.ExpenseDetails.as_view(), name='expense_detail'),
    path('create', views.ExpenseCreate.as_view(), name='expense_create'),
    path('update/<int:pk>', views.ExpenseUpdate.as_view(), name='expense_update'),
    path('delete/<int:pk>', views.ExpenseDelete.as_view(), name='expense_delete'),
    path('show',views.show),
    path('hello',views.hello_world),
]
