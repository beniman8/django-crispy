from django import forms
from .models import CandidateModel


class CandidateForm(forms.ModelForm):

    class Meta:
        model = CandidateModel
        fields = "__all__"