from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import GroceryForm
from .models import Grocery
from .models import Grocery
# Create your views here.
def AddGrocery(request):
    form = GroceryForm()
    if request.method == 'POST':
        form = GroceryForm(request.POST)
        if form.is_valid():
            grocery = form.cleaned_data['groceryitems']
            price = int(form.cleaned_data['price'])
            date = form.cleaned_data['date']
            dp = price - price * 0.10
            obj = Grocery(groceryitems=grocery, price=price, Discounts=dp, date=date)
            obj.save()
            return redirect('showgrocery_url')
    template_name = 'groceryapp/grocery.html'
    context = {'form':form }
    return render(request, template_name, context)

def ShowGrocery(request):
    obj = Grocery.objects.all()
    template_name = 'groceryapp/showgrocery.html'
    context = {'obj':obj}
    return render(request, template_name, context)



