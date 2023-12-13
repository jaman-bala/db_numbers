from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Add_Numbers, Category_Number, Category_Unaa, Category_Region
from .forms import CreateForm


def get_index(request):
    add_numbers = Add_Numbers.objects.all()
    add_number = Add_Numbers.objects.order_by('-id')
    qs_region = Category_Region.objects.all()
    qs_number = Category_Number.objects.all()
    qs_unaa = Category_Unaa.objects.all()

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

    context = {'add_number': add_number,
               'add_numbers': add_numbers,
               'qs_region': qs_region,
               'qs_number': qs_number,
               'qs_unaa': qs_unaa,
               'form': form,
               'error': error
               }
    return render(request, 'allgosnumbers/index.html', context)
