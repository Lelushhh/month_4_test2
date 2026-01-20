from django.shortcuts import render
from .models import ClothesModel, Brand

def clothes_list(request):
    brand_id = request.GET.get('brand')

    clothes = ClothesModel.objects.all()
    if brand_id:
        clothes = clothes.filter(brands__id=brand_id)

    brands = Brand.objects.all()

    return render(request, 'clothes.html', {
        'clothes': clothes,
        'brands': brands
    })
