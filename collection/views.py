from django.shortcuts import render
from collection.models import Pharmacist


# Create your views here.
def index(request):
	pharmacist = Pharmacist.objects.all()
	
	return render(request, 'index.html',{
		'pharmacist': pharmacist,
		})