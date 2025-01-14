from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from dashboard.models import MarqueeText
from .models import Product, CustomOrderItem, EquipmentCheckout
from .forms import ProductForm, CustomOrderItemForm, EquipmentCheckoutForm

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
    # Threshold for low stock
    threshold = 10
    low_stock_items = Product.objects.exclude(category='Equipment').filter(quantity__lt=threshold).order_by('category', 'name')

    # Handle custom item addition
    if request.method == 'POST':
        form = CustomOrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-staff')
    else:
        form = CustomOrderItemForm()

    # Fetch existing custom items
    custom_items = CustomOrderItem.objects.all().order_by('name')

    context = {
        'items': low_stock_items,
        'custom_items': custom_items,
        'custom_form': form,
    }
    return render(request, 'dashboard/staff.html', context)

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


def delete_custom_item(request, pk):
    custom_item = get_object_or_404(CustomOrderItem, pk=pk)
    custom_item.delete()
    return redirect('dashboard-staff')

def equipment_page(request):
    # Filter equipment items
    equipment_items = Product.objects.filter(category='Equipment')

    # Handle form submission for checking out equipment
    if request.method == 'POST':
        form = EquipmentCheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_page')
    else:
        form = EquipmentCheckoutForm()

    # Get all checkouts
    checkouts = EquipmentCheckout.objects.filter(checked_in_at__isnull=True)
    checked_out_ids = checkouts.values_list('equipment_id', flat=True)
    context = {
        'equipment_items': equipment_items,
        'checkouts': checkouts,
        'checked_out_ids': list(checked_out_ids),
        'form': form,
    }
    return render(request, 'dashboard/equipment.html', context)

def checkout_equipment(request):
    if request.method == 'POST':
        form = EquipmentCheckoutForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('equipment_page')

def checkin_equipment(request, pk):
    checkout = get_object_or_404(EquipmentCheckout, pk=pk)
    checkout.checked_in_at = timezone.now()
    checkout.save()
    return redirect('equipment_page')
