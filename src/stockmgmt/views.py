from django.shortcuts import render, redirect
from .models import *
from.forms import StockCreateForm,StockSearchForm,StockUpdateForm

# Create your views here.
def home(request):
    title = 'Home'
    message = 'Welcome to Home page'

    context={
        "title":title,
		"message":message,
    }
    return render(request , "home.html", context)

def list_items(request):
	title = 'list_items'
	header = 'List of the items'
	form = StockSearchForm(request.POST or None)
	queryset = Stock.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
		"header": header,
		"form": form,
	}
	if request.method == 'POST':
		queryset = Stock.objects.filter(category__icontains=form['category'].value(),
										item_name__icontains=form['item_name'].value())
		context = {
		"title": title,
		"form": form,
		"header": header,
		"queryset": queryset,
		}
	return render(request, "list_items.html", context)




def add_items(request):
	form = StockCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('list_items')

	context ={
		"form": form,
		"title": 'Add Item',
	}
	return render(request, "add_items.html",context)


def update_items(request, pk):
	queryset = Stock.objects.get(id= pk)
	form = StockUpdateForm(instance = queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance = queryset)
		if form.is_valid():
			form.save()
			return redirect('/list_items')
	context ={
		'form' : form
	}
	return render(request, 'add_items.html', context)


def delete_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/list_items')
	return render(request, 'delete_items.html')
