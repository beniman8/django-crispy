from django import forms
from .models import CandidateModel,SMOKER
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

    experience = forms.BooleanField(label="I have experience", required = False)

    message = forms.CharField(
        label="About Yourself",
        min_length=50,
        max_length=1000,
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Tell me about yourself...",
                "rows": 4,
            }
        ),
    )

    # Way to generatefield
    # GENDER = [('M','Male'),('F','Female')]
    # gender = forms.CharField(label='Gender',widget=forms.RadioSelect(choices=GENDER))

    class Meta:
        model = CandidateModel
        # fields = "__all__"
        # fields = ['firstname','lastname','email','age','message']
        exclude = ["created_at", "status"]

        #Label Control
        labels = {
            'personality':'Choose a personality',
            'salary':'Choose a salary',
            'gender':'Your Gender',
            'smoker':'Do you smoke',                        
        }


        SALARY = (
            ("", "Salery expectation per (month)"),
            ("Between ($3000 and $4000)", "Between ($3000 and $4000)"),
            ("Between ($4000 and $5000)", "Between ($4000 and $5000)"),
            ("Between ($5000 and $7000)", "Between ($5000 and $7000)"),
            ("Between ($7000 and $10000)", "Between ($7000 and $10000)"),
        )

        # way to generate gender
        GENDER = [("M", "Male"), ("F", "Female")]

        # Third party Widget
        widgets = {
            "phone": forms.TextInput(
                attrs={
                    "style": "font-size: 13px",
                    "placeholder": "Phone",
                    "data-mask": "(000) 000-0000",
                }
            ),
            "salary": forms.Select(
                choices=SALARY,
                attrs={
                    "class": "form-control",  # booostrap inside the form.py
                },
            ),
            "gender": forms.RadioSelect(choices=GENDER, attrs={"class": "btn-check"}),
            "smoker": forms.RadioSelect(choices=SMOKER,attrs={"class": "btn-check"}),
        }


    # Super function

    def __init__(self, *args, **kwargs):

        ''' You can control all of your fields in the ini method'''
        super(CandidateForm,self).__init__(*args, **kwargs)
        

        # ==Control Panel Optional control method==

        #input required
        # self.fields['message'].required = False

        #disable input 
        # self.fields['experience'].disabled = True

        #Input readonly
        # self.fields['email'].widget.attrs.update({'readonly':'readonly'})

        # ==Select option controls==
        self.fields['personality'].choices = [('','Select a personality'),] + list(self.fields['personality'].choices)[1:]

        # ==Widget control==

        #This is how you over ride fields in a widget
        # self.fields['phone'].widget.attrs.update({'style':'font-size: 18px'})
        
        
        #Using loop to disable/readonly multiple fields 

        # readonly=['firstname','lastname','job']
        # for field in readonly:
        #     self.fields[field].widget.attrs['readonly'] = 'true'

        # disabled =['gender','smoker']
        # for field in disabled:
        #     self.fields[field].widget.attrs['disabled'] = 'true'