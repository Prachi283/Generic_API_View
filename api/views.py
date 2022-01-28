# GenericAPIView and Mixin
# pk== primary key 
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# List and Create = pk not required 
class LCEmployeeAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
	queryset= Employee.objects.all()
	serializer_class = EmployeeSerializer

	def get(self,request,*args,**kwargs):
		return self.list(request,*args,**kwargs)

	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

# Retrieve, Update and Delete required pk 
class RUDEmployeeAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
	queryset= Employee.objects.all()
	serializer_class = EmployeeSerializer

	def get(self,request,*args,**kwargs):
		return self.retrieve(request,*args,**kwargs)

	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)

