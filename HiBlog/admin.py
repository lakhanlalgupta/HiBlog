from django.contrib import admin

# Register your models here.
from .models import NewSubjects
from .models import Data
admin.site.register(NewSubjects)
admin.site.register(Data)