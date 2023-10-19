from django.shortcuts import render

# Create your views here.

from .models import Supplier, Part
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})