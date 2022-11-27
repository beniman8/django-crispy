from django.db import models

STATUS = (
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Disapproved','Disapproved'),
)


PERSONALITY_TYPE=(
    ('outgoing','outgoing'),
    ('sociable','sociable'),
    ('antisocial','antisocial'),
    ('discreet','discreet'),
    ('serious','serious'),
)

SMOKER = (
    ('1','Yes'),
    ('2','No'),
)


class CandidateModel(models.Model):

    firstname = models.CharField(max_length=50)
    lastname =  models.CharField(max_length=50)
    job =  models.CharField(max_length=5)
    age =  models.CharField(max_length=3)
    phone = models.CharField(max_length=25)
    personality = models.CharField(max_length=50, null=True,choices=PERSONALITY_TYPE)
    salary = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    experience = models.BooleanField(null=True)
    smoker = models.CharField(max_length=10, null=True,choices=SMOKER,default="")
    email  = models.EmailField( max_length=254)
    message =  models.TextField()
    file = models.FileField()
    created_at = models.DateTimeField( auto_now=False, auto_now_add=True)
    status = models.CharField(max_length=50, null=True,choices=STATUS,default='Pending')


    #Capitalize the names 
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()
    

    def __str__(self):
        return self.firstname
