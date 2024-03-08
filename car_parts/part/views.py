from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Part
from .forms import NewPartForm, SearchPartForm

@login_required
def results(request):
    if request.method == 'GET':
        model_query = request.GET.get('model', '')
        year_query = request.GET.get('year', '')
        power_query = request.GET.get('power', '')
        consumption_query = request.GET.get('consumption', '')
        transmission_query = request.GET.get('transmission', '')
        title_query = request.GET.get('title', '')
        brand_query = request.GET.get('brand', '')
        condition_query = request.GET.get('condition', '')
        description_query = request.GET.get('description', '')
        form = SearchPartForm()
        """
        parts is a queryset of Part objects that match the search criteria
        where it matches the model, year, power, consumption, transmission, title, brand, condition, and description together
        if a field is empty, it is not included in the search

        Use Postgres search to search for the fields
        """
        parts = Part.objects.annotate(
            search=SearchVector('model', 'year', 'power', 'consumption', 'transmission', 'title', 'brand', 'condition', 'description')
        ).filter(
            search=SearchQuery(model_query) & SearchQuery(year_query) & SearchQuery(power_query) & SearchQuery(consumption_query) & SearchQuery(transmission_query) & SearchQuery(title_query) & SearchQuery(brand_query) & SearchQuery(condition_query) & SearchQuery(description_query)
        )

        print(parts)
        
        
        return render(request, 'part/results.html', {
            'parts': parts,
            'form': form
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
        form = NewPartForm(request.POST, request.FILES)
        if form.is_valid():
            part = form.save(commit=False)
            part.created_by = request.user
            part.save()
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
            part.quantity -= 1
            part.save()
            return redirect('part:part_details', pk=part.pk)
        part.delete()
        return redirect('core:index')

@login_required
def add_more(request, pk):
    part = get_object_or_404(Part, pk=pk)
    if request.method == 'GET':
        if part.quantity >= 0:
            part.quantity += 1
            part.save()
            return redirect('part:part_details', pk=part.pk)