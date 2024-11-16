from django.shortcuts import render, redirect
from .models import Restaurant
import qrcode
import os
from django.conf import settings

def index(request):
    if request.method == "POST":
        restaurant_name = request.POST.get('restaurant_name')
        menu_link = request.POST.get('menu_link')

        # Generate QR Code
        obj = qrcode.make(menu_link)
        file_name = restaurant_name.replace(" ", "_") + "_menu.png"
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        obj.save(file_path)

        # Create Image URL
        qr_code_url = f"{settings.MEDIA_URL}{file_name}"

        restaurant = Restaurant.objects.create(
            name=restaurant_name,
            url=menu_link
        )
        restaurant.save()

        context = {
            "restaurant_name": restaurant_name,
            "qr_code_url": qr_code_url
        }
        return render(request, 'qr-result.html', context)
    else:
        return render(request, 'index.html')
