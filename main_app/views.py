from django.shortcuts import render
from .models import Treasure

from django.http import HttpResponse


# Create your views here.

def index(request):
    treasures = Treasure.objects.all()
    return render(request,'index.html', {'treasures' : treasures})

# class Treasure:
#     def __init__(self, name, value, material, location, img_url):
#         self.name = name
#         self.value = value
#         self.material = material
#         self.location = location
#         self.img_url = img_url
#
# treasures = [
#     Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM", 'http://weknowyourdreams.com/images/tree/tree-06.jpg'),
#     Treasure("Fools Gold", 0, 'pyrite', 'Fools Fall, CO', 'http://wallpaper-gallery.net/images/images-of-trees/images-of-trees-4.jpg' ),
#     Treasure("Coffee Can", 20.00, 'tin', 'Acme , CA', 'http://wallpaper-gallery.net/images/images-of-trees/images-of-trees-11.jpg'),
# ]