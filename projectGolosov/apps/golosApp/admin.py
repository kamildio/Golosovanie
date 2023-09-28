from django.contrib import admin
from .models import CanditeForm

@admin.register(CanditeForm)
class CandidateFormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bio', 'birthdate', 'image', 'partiya')
    search_fields = ('first_name', 'last_name', 'partiya')