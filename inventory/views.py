from django.shortcuts import render

from django.http import Http404

#from django.http import HttpResponse (no longer needed in IMPLEMTING VIEWS section of course because
# now using render(...) to wire request to a template

from inventory.models import Item

def index(request):
	items = Item.objects.exclude(amount=0)
	return render(request, 'inventory/index.html', {
			'items': items,
	})
	#return HttpResponse('<p>In index view</p>') 

def item_detail(request, id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request, 'inventory/item_detail.html', {
		'item': item,
	})

def backorder_detail(request, id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request, 'inventory/backorder_detail.html', {
		'item': item,
	})

	#return HttpResponse('<p>In item_detail view with id {0}</p>'.format(id))
