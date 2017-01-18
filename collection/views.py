from django.shortcuts import render
from collection.forms import PharmacistForm
from collection.models import Pharmacist


# Create your views here.
def index(request):

	pharmacists = Pharmacist.objects.all()
	
	return render(request, 'index.html',{
		'pharmacists': pharmacists,
		})

def pharmacist_detail(request, slug):
	#grab the object
	pharmacist = Pharmacist.objects.get(slug=slug)
	#and pass to the template
	return render(request, 'pharmacists/pharmacist_detail.html', {
		'pharmacist': pharmacist,
		})

def edit_pharmacist(request, slug):
	#grab the object
	pharmacist = Pharmacist.objects.get(slug=slug)
	#set the form we're using
	form_class = PharmacistForm
	#if we're coming to this view from a submitted form:
	if request.method == 'POST':
		#grab the data from a submitted form
		form = form_class(data=request.POST, instance=pharmacist)
		if form.is_valid():
			#save the new data
			form.save()
			return redirect('pharmacist_detail', slug=pharmacist.slug)
	else: #otherwise just create the form
		form = form_class(instance=pharmacist)
	#and render the template
	return render(request, 'pharmacists/edit_pharmacist.html', {
		'pharmacist': pharmacist,
		'form': form,
		})