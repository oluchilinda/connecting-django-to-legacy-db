from django.urls import path
from.views import ListEmployee, DetailEmployee

urlpatterns = [
    path("", ListEmployee.as_view(), name="employee_list"),
    path("<int:pk>/", DetailEmployee.as_view(), name="employee_detail")
]