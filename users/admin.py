from django.contrib import admin
from users.models import CustomUser
from users.models import Location
from users.models import HorseTour
from users.models import TourRegistration

admin.site.register(CustomUser)
admin.site.register(Location)
admin.site.register(HorseTour)
admin.site.register(TourRegistration)