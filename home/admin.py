from django.contrib import admin
# Register your models here.
from home.models import Register,CallRecording
admin.site.register(CallRecording)
admin.site.register(Register)