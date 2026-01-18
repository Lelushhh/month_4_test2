from django.shortcuts import render, redirect, get_object_or_404
from basket.forms import BasketForm
from basket.models import Basket

def create_basket_view(request):
     if request.method == 'POST':
        form = BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/basket_list/')
     else:
        form = BasketForm()
     return render(
         request,
         template_name='basket/create_basket.html',
         context={"form": form}
     )


#READ
def read_basket_view(request):
    if request.method == 'GET':
        basket = Basket.objects.all()
    return render(request, template_name='basket/basket_list.html',
                  context={'basket': basket})    


#update
def update_basket_view(request, id):
    basket_id = get_object_or_404(Basket, id=id)
    if request.method == 'POST':
        form = BasketForm(request.POST, instance=basket_id)
        if form.is_valid():
            form.save()
            return redirect('/basket_list/')
    else: 
        form = BasketForm(instance=basket_id)
    return render(request,
                  template_name='basket/update_basket.html',
                  context={
                      'form': form,
                      'basket_id': basket_id
                  }
                )
#delete
def delete_basket_view(request, id):
    basket_id = get_object_or_404(Basket, id=id)
    basket_id.delete()
    return redirect('/basket_list/')