from django.contrib import admin
from catalog.models import Variation,Product,ImageProduct
# Register your models here.

class ImageProductInline(admin.TabularInline):
    model = ImageProduct
    extra = 0
    raw_id_fields = ('product',) 

class VariationInline(admin.TabularInline):
    model = Variation
    extra = 0
    raw_id_fields = ('product',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (ImageProductInline,VariationInline)


admin.site.register(Variation)
admin.site.register(Product,ProductAdmin)
admin.site.register(ImageProduct)
