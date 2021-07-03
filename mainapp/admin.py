from django.contrib import admin
from .models import Question,Category,Number,Item,Variant,Benchmark,Material
# Register your models here.
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Number)
admin.site.register(Variant)
admin.site.register(Benchmark)
admin.site.register(Material)
admin.site.register(Item)
