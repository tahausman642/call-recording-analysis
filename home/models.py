from django.db import models

'''
#make migrations - create changes and store in a file
#migrate - apply the changes to the database used, created by makemigrations
'''
'''
python manage.py shell
from home.models import Login
Login.objects.all()
Login.objects.filter(name="taha")
'''

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=120)
    username=models.CharField(primary_key=True,max_length=120)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
    
class CallRecording(models.Model):
    UPLOAD_STATUS = [
        ('UPLOADING', 'Uploading'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed')
    ]
    
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='recordings/%Y/%m/%d/')
    upload_date = models.DateTimeField('Date added')
    #call_date = models.DateTimeField(null=True, blank=True)
    #caller_number = models.CharField(max_length=20, blank=True)
    #status = models.CharField(max_length=10, choices=UPLOAD_STATUS, default='UPLOADING')
    #duration = models.PositiveIntegerField(default=0)  # in seconds

    def __str__(self):
        return f"{self.user.username}'s recording from {self.upload_date}"
    