from django.contrib import admin

# Register your models here.
from . models import Genre, IdiomaTx, IdiomaAu, VG, VGInstance, Dev, Pub, Rating, Plat

admin.site.register(Genre)
admin.site.register(IdiomaTx)
admin.site.register(IdiomaAu)
admin.site.register(VG)
admin.site.register(VGInstance)
admin.site.register(Dev)
admin.site.register(Pub)
admin.site.register(Rating)
admin.site.register(Plat)