from django.shortcuts import render, redirect
from django.http import HttpResponse

from dashboard.models import MarqueeText
from .models import Product
from .forms import ProductForm

# Create your views here.

def index(request):
    marquee_text = MarqueeText.objects.first()
    items = Product.objects.order_by('category', 'name')

    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = ProductForm()
    context={
        'items': items,
        'marquee_text': marquee_text,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)

def staff(request):
    return render(request, 'dashboard/staff.html')

def admin(request):
    return render(request, 'admin.html')

from django.shortcuts import get_object_or_404, redirect
from .models import Product

def add_quantity(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        try:
            quantity_to_add = int(request.POST.get('quantity', 0))
            product.quantity += quantity_to_add
            product.save()
        except ValueError:
            pass  # Handle invalid input gracefully
    return redirect('dashboard-index')  # Replace 'your_table_page' with the name of your page's URL pattern

def remove_quantity(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        try:
            quantity_to_remove = int(request.POST.get('quantity', 0))
            if product.quantity >= quantity_to_remove:
                product.quantity -= quantity_to_remove
                product.save()
        except ValueError:
            pass  # Handle invalid input gracefully
    return redirect('dashboard-index')  # Replace 'your_table_page' with the name of your page's URL pattern
