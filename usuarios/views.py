from django.shortcuts import render,HttpResponse
from rolepermissions.decorators import has_permission_decorator

@has_permission_decorator('cadastrar_vendedor')
def cadastar_vendedor(request):
	return render(request,'cadastrar_vendedor.html')