from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Part, SaleHistory
from .forms import NewPartForm, SearchPartForm
import datetime

@login_required
def results(request):
    if request.method == 'POST':
        model_query = request.POST.get('model', '')
        year_query = request.POST.get('year', '')
        power_query = request.POST.get('power', '')
        consumption_query = request.POST.get('consumption', '')
        transmission_query = request.POST.get('transmission', '')
        title_query = request.POST.get('title', '')
        brand_query = request.POST.get('brand', '')
        condition_query = request.POST.get('condition', '')
        form = SearchPartForm()

        parts = Part.objects.filter(
            Q(model__iexact=model_query) |
            Q(year__iexact=year_query) |
            Q(power__iexact=power_query) |
            Q(consumption__iexact=consumption_query) |
            Q(transmission__iexact=transmission_query) |
            Q(title__iexact=title_query) |
            Q(brand__iexact=brand_query) |
            Q(condition__iexact=condition_query)
            ).distinct()

        return render(request, 'part/results.html', {
            'form': form,
            'parts': parts
        })


@login_required
def search(request):
    parts = Part.objects.all()
    form = SearchPartForm()
    title = 'Search Part'

    return render(request, 'part/search.html', {
        'form': form,
        'title': title,
        'parts': parts
    })

@login_required
def part_details(request, pk):
    part = get_object_or_404(Part, pk=pk)
    
    return render(request, 'part/part_details.html' ,{
        'part': part
    })

@login_required
def new_part(request):
    if request.method == 'POST':
        print(f"\n\nPOST: {request.POST}")
        form = NewPartForm(request.POST, request.FILES)
        if form.is_valid():
            part = form.save(commit=False)
            part.created_by = request.user
            part.save()
            SaleHistory.objects.create(part=part, sold=False, available=part.quantity)
            return redirect('part:part_details', pk=part.pk)
    else:
        form = NewPartForm()
    return render(request, 'part/new_part.html', {
        'form': form,
        'title': 'Add Product'
    })

@login_required
def sell_part(request, pk):
    part = get_object_or_404(Part, pk=pk)
    if request.method == 'GET':
        if part.quantity > 0:
            part.sell_part()
            return redirect('part:part_details', pk=part.pk)
        part.delete()
        return redirect('core:index')

@login_required
def add_more(request, pk):
    part = get_object_or_404(Part, pk=pk)
    if request.method == 'GET':
        if part.quantity >= 0:
            part.add_quantity(1)
            part.save()
            return redirect('part:part_details', pk=part.pk)

@login_required
def sold_parts(request):
    sale_history = SaleHistory.objects.all().order_by('-sold_at').all()
    print(f"Parts: {sale_history}")
    title = 'Sold History'
    return render(request, 'part/sold_history.html', {
        'sale_history': sale_history,
        'title': title
    })