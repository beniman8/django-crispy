from django import forms
from .models import CandidateModel
from django.core.validators import RegexValidator

# Lower  case every letter
class LowerCase(forms.CharField):
    def to_python(self, value):
        return value.lower()


# Upper  case every letter
class UpperCase(forms.CharField):
    def to_python(self, value):
        return value.upper()


class CandidateForm(forms.ModelForm):

    # validations
    firstname = forms.CharField(
        label="First Name",
        min_length=3,
        max_length=50,
        required=True,
        validators=[
            RegexValidator(r"^[a-zA-ZÀ-ÿ\s]*$", message="Only letters is allowed !")
        ],
        # local widget
        widget=forms.TextInput(attrs={"placeholder": "First name"}),
    )

    lastname = forms.CharField(
        label="Last Name",
        min_length=3,
        max_length=50,
        required=True,
        validators=[
            RegexValidator(r"^[a-zA-ZÀ-ÿ\s]*$", message="Only letters is allowed !")
        ],
        widget=forms.TextInput(attrs={"placeholder": "Last name"}),
    )

    job = UpperCase(
        label="Job code",
        min_length=5,
        max_length=5,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Example: FR-22"}),
    )

    email = LowerCase(
        label="Email Address",
        min_length=6,
        max_length=50,
        required=True,
        validators=[
            RegexValidator(
                r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", message="Email not valid"
            )
        ],
        widget=forms.TextInput(attrs={"placeholder": "Email"}),
    )

    age = forms.CharField(
        label="Age",
        min_length=2,
        max_length=3,
        required=True,
        validators=[RegexValidator(r"^[0-9]*$", message="Only numbers please !")],
        widget=forms.TextInput(attrs={"placeholder": "Age"}),
    )

    message = forms.CharField(
        label="About Yourself",
        min_length=50,
        max_length=1000,
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Tell me about yourself...",
                "rows": 10,
            }
        ),
    )

    class Meta:
        model = CandidateModel
        # fields = "__all__"
        # fields = ['firstname','lastname','email','age','message']
        exclude = ["created_at", "status"]

        # Third party Widget
        widgets = {
            "phone": forms.TextInput(
                attrs={
                    "style": "font-size: 13px",
                    "placeholder": "Phone",
                    "data-mask": "(000) 000-0000",
                }
            )
        }
