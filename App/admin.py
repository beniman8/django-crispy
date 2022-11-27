from django.contrib import admin
from .forms import CandidateForm
from .models import CandidateModel
from django.utils.html import format_html


class CandidateAdmin(admin.ModelAdmin):
    radio_fields = {"smoker": admin.HORIZONTAL}
    form = CandidateForm
    readonly_fields = [
        "firstname",
        "lastname",
        "experience",
        "email",
        "job",
        "age",
        "phone",
        "personality",
        "salary",
        "gender",
        "smoker",
        "message",
        "file",
        'frameworks',
        'languages',
        'databases',
        'libraries',
        'mobile',
        'other',
    ]
    exclude = ['status_color']
    list_filter = ["status"]
    list_display = (
        "firstname",
        "lastname",
        "email",
        "job",
        "age",
        "created_at",
        "status_color",
        "_",
    )
    search_fields = ["firstname", "lastname", "email", "job", "age", "status"]
    list_per_page = 10

    # change icons
    def _(self, obj):
        if obj.status == "Approved":
            return True
        elif obj.status == "Pending":
            return None
        else:
            return False

    _.boolean = True

    # change text color
    def status_color(self, obj):
        if obj.status == "Approved":
            color = "#28a745"
        elif obj.status == "Pending":
            color = "#fea95e"
        else:
            color = "red"

        return format_html(
            f'<strong><p style="color: {color}">{obj.status}</p></strong>'
        )

    status_color.allow_tags = True


admin.site.register(CandidateModel, CandidateAdmin)
