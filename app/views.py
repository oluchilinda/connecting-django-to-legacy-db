
from rest_framework import generics 
from.bank_models import Employee
from.serializers import EmployeeSerializer

class ListEmployee(generics.ListAPIView):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer

class DetailEmployee(generics.RetrieveAPIView):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer