from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Add_Numbers, Category_Number, Category_Unaa, Category_Types
from .forms import CreateForm


def get_index(request):
    add_numbers = Add_Numbers.objects.all()
    qs_region = Category_Types.objects.filter(add_numbers__in=add_numbers).distinct()
    qs_number = Category_Number.objects.filter(add_numbers__in=add_numbers).distinct()
    qs_unaa = Category_Unaa.objects.filter(add_numbers__in=add_numbers).distinct()

    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        error = 'Формат был неверной'
        form = CreateForm()

    page = request.GET.get('page', 1)
    paginator = Paginator(add_numbers, 15)  # Показывать 15 камер на странице
    try:
        add_numbers = paginator.page(page)
    except PageNotAnInteger:
        add_numbers = paginator.page(1)
    except EmptyPage:
        add_numbers = paginator.page(paginator.num_pages)

    context = {
               'add_numbers': add_numbers,
               'qs_region': qs_region,
               'qs_number': qs_number,
               'qs_unaa': qs_unaa,
               'form': form,
               'error': error
               }
    return render(request, 'allgosnumbers/index.html', context)


def unaa_detail(request, unaa_id):
    unaa = get_object_or_404(Category_Unaa, id=unaa_id)
    add_numbers = Add_Numbers.objects.filter(category_unaa=unaa,)

    context = {
        'add_numbers': add_numbers,
        'unaa': unaa,
    }

    return render(request, 'allgosnumbers/unaa_detail.html', context)