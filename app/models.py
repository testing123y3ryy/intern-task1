from django.db import  models
from django.core.validators import MinLengthValidator
import datetime
from django.utils.timezone import now
import os

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Patient(models.Model):
    image = models.ImageField(upload_to=filepath, null=True , blank=True)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    DorP = models.CharField(max_length=2, default='1')
    line1 = models.TextField(max_length=500)
    state = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    pincode = models.PositiveBigIntegerField()
    password = models.CharField(max_length=500)
    cpassword = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_patient_by_email(email):
        try:
            return Patient.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Patient.objects.filter(email = self.email):
            return True

        return  False

    def isExistsByUsername(self):
        if Patient.objects.filter(username = self.username):
            return True

        return  False


    def __str__(self):
        return self.first_name +" " + self.last_name

STATUS_CHOICES = (
	('draft','Draft'),
	('published', 'Published'),
)


class Category(models.Model):
	title = models.CharField(max_length=100, verbose_name='Title')
		
	def __str__(self):
		return self.title


class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True)
	status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10)
	publication_date = models.DateTimeField(default=now)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	picture = models.ImageField(upload_to=filepath, null=True , blank=True)
	summary = models.TextField(max_length=1000)
	content = models.TextField(max_length=1000)
	author = models.CharField(max_length=30)
		
	def __str__(self):
		return self.title
