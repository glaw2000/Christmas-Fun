from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import WishList, Coal

# Register your models here.
admin.site.register(WishList)
admin.site.register(Coal)
