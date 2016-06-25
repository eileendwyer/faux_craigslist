from django.contrib import admin

from tootieapp.models import Category, Posting, Village, Profile


admin.site.register (Category)
admin.site.register(Posting)
admin.site.register(Village)
admin.site.register(Profile)
