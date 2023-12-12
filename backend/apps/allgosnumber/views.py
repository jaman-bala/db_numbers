from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Add_Numbers, Category_Number, Category_Unaa, Category_Region


def get_category_region(request):
    regions = Category_Region.objects.all()
    context = {'regions': regions}
    return render(request, 'index.html', context)


def get_index(request):
    add_numbers = Add_Numbers.objects.all()
    add_number = Add_Numbers.objects.order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(add_numbers, 15)  # Показывать 15 камер на странице
    try:
        add_numbers = paginator.page(page)
    except PageNotAnInteger:
        add_numbers = paginator.page(1)
    except EmptyPage:
        add_numbers = paginator.page(paginator.num_pages)

    context = {'add_number': add_number,
               'add_numbers': add_numbers,
               }
    return render(request, 'allgosnumbers/index.html', context)