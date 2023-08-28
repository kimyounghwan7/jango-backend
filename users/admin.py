from django.contrib import admin
from .models import User, UserImage

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ['userName']

admin.site.register(User)
