from django.db import models
from multiselectfield import MultiSelectField


STATUS = (
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Rejected", "Rejected"),
)


PERSONALITY_TYPE = (
    ("outgoing", "outgoing"),
    ("sociable", "sociable"),
    ("antisocial", "antisocial"),
    ("discreet", "discreet"),
    ("serious", "serious"),
)

SMOKER = (
    ("1", "Yes"),
    ("2", "No"),
)


FRAMEWORKS = (
    ("Laravel", "Laravel"),
    ("Angular", "Angular"),
    ("Django", "Django"),
    ("Flask", "Flask"),
    ("Vue", "Vue"),
    ("Others", "Others"),
)

LANGUAGES = (
    ("Python", "Python"),
    ("Javascript", "Javascript"),
    ("Java", "Java"),
    ("C++", "C++"),
    ("Ruby", "Ruby"),
    ("Rust", "Rust"),
    ("C#", "C#"),
    ("Others", "Others"),
)

DATABASES = (
    ("MySql", "MySql"),
    ("Postgres", "Postgres"),
    ("MongoDB", "MongoDB"),
    ("SqLite3", "SqLite3"),
    ("Oracle", "Oracle"),
    ("Others", "Others"),
)

LIBRARIES = (
    ("Ajax", "Ajax"),
    ("Jquery", "Jquery"),
    ("React", "React"),
    ("Chart.js", "Chart.js"),
    ("Gsap", "Gsap"),
    ("Others", "Others"),
)

MOBILE = (
    ("React native", "React native"),
    ("Kivy", "Kivy"),
    ("Flutter", "Flutter"),
    ("Ionic", "Ionic"),
    ("Xamarim", "Xamarim"),
    ("Others", "Others"),
)

OTHERS = (
    ("UML", "UML"),
    ("SQL", "SQL"),
    ("Docker", "Docker"),
    ("Git", "Git"),
    ("GraphQL", "GraphQL"),
    ("Others", "Others"),
)


class CandidateModel(models.Model):

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=25)
    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY_TYPE)
    salary = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    experience = models.BooleanField(null=True)
    smoker = models.CharField(max_length=10, null=True, choices=SMOKER, default="")
    email = models.EmailField(max_length=254)
    message = models.TextField()
    file = models.FileField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.CharField(
        max_length=50, null=True, choices=STATUS, default="Pending"
    )

    # Multiple Checkboxes
    frameworks = MultiSelectField(choices=FRAMEWORKS, default="",max_length=25)
    languages = MultiSelectField(choices=LANGUAGES, default="",max_length=25)
    databases = MultiSelectField(choices=DATABASES, default="",max_length=25)
    libraries = MultiSelectField(choices=LIBRARIES, default="",max_length=25)
    mobile = MultiSelectField(choices=MOBILE, default="",max_length=25)
    other = MultiSelectField(choices=OTHERS, default="",max_length=25)

    # Capitalize the names
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    
    def name(self):
        return f"{self.firstname} {self.lastname}"
