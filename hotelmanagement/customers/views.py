from django.shortcuts import render, redirect
from .models import Customers

# Create your views here.


def index(request):
    customers = Customers.objects.all()
    context = {'customers': customers}
    context['customers_navlink'] = True
    return render(request, 'customers/index.html', context)


def onGetCreate(request):
    context = {}
    context['customers_navlink'] = True
    return render(request, 'customers/create.html', context)


def onPostCreate(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        postal_code = request.POST.get('postal_code')
        city = request.POST.get('city')
        country = request.POST.get('country')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        customers = Customers(first_name=first_name, last_name=last_name, address=address,
                              postal_code=postal_code, city=city, country=country, email=email, phone=phone)
        customers.save()
    return redirect('customers:index')


def onGetEdit(request, id):
    customers = Customers.objects.get(id=id)
    context = {'customers': customers}
    return render(request, 'customers/edit.html', context)


def onPostEdit(request, id):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        postal_code = request.POST.get('postal_code')
        city = request.POST.get('city')
        country = request.POST.get('country')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        Customers.objects.filter(id=id).update(first_name=first_name, last_name=last_name, address=address,
                                               postal_code=postal_code, city=city, country=country, email=email, phone=phone)
    return redirect('customers:index')


def onPostDelete(request, id):
    if request.method == "GET":
        customer = Customers.objects.get(id=id)
        customer.delete()
    return redirect('customers:index')
