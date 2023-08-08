from django.contrib import admin

# Register your models here.

from .models import Contact
from .models import Profile
from .models import Country
from .models import City
from .models import Field
from .models import Task

admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Field)
admin.site.register(Task)