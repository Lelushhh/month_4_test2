from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from products.models import Products

def product(request):
    if request.method == "GET":
        product = Products.objects.all()
    return render(
        request,
        template_name='blog/blog_list.html',
        context={
            'product':product
        }
    )

def product_detail(request,id):
    if request.method == "GET":
        product_id = get_object_or_404(Products, id=id)
    return render(
        request,
        template_name='blog/blog_detail.html',
        context={
            'product_id': product_id
        }
    )



def korean_products(request):
    if request.method == 'GET':
        return HttpResponse("""ТОП 5 продуктов в корее:
        1:Кимчи
        2:Бимимбап
        3:Ттокбокки
        4:Булгоги
        5:Корейский фрайд чикен""")

def data_time(request):
    if request.method == 'GET':
        now = datetime.now()
        return HttpResponse(
            f"Дата: {now.strftime('%d.%m.%Y')}\n"
            f"Время: {now.strftime('%H:%M:%S')}" ,
        )
    
def about_myself(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://images.unsplash.com/photo-1526779259212-939e64788e3c?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D">' \
        '<p> Меня зовут Абидин, и я сейчас делаю дз <p/>')