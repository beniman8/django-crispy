from django.contrib import admin

from .models import CandidateModel



class CandidateAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','email')
    search_fields = ['firstname','lastname','email']
    list_per_page = 10

admin.site.register(CandidateModel, CandidateAdmin)




