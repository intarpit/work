from django.shortcuts import render
from .models import wash_basin
from django.core.paginator import Paginator

# Create your views here.

def item_display(request):
    
    items = wash_basin.objects.all()
    pages = Paginator(items, 8)
    page_num = request.GET.get('page', 1)
    items = pages.get_page(page_num)

    wash_basin_dict = {
        'items': items
    }
    
    return render(request, 'wash_basin.html', wash_basin_dict)


def item_detail(request):

    wash_basin_detail = {
        
    }

    return render(request, 'wash_basin_detail.html', wash_basin_detail)