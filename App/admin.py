from django.contrib import admin

from .models import CandidateModel
from django.utils.html import format_html


class CandidateAdmin(admin.ModelAdmin):
    list_filter = ['status']
    list_display = ('firstname','lastname','email','job','age','created_at','status_color','_')
    search_fields = ['firstname','lastname','email','job','age','status']
    list_per_page = 10


    #change icons 
    def _(self,obj):
        if obj.status == "Approved":
            return True
        elif obj.status == "Pending":
            return None
        else:
            return False

    _.boolean=True

    # change text color
    def status_color(self,obj):
        if obj.status == "Approved":
            color = '#28a745'  
        elif obj.status == "Pending":
            color = '#fea95e'
        else:
            color = 'red'
        
        return format_html(f'<strong><p style="color: {color}">{obj.status}</p></strong>')

    status_color.allow_tags = True


admin.site.register(CandidateModel, CandidateAdmin)




