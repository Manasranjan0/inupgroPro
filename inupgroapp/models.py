from django.db import models
# Create your models here.
class host_UserData(models.Model):
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,unique=True,blank=True,null=True)
    password=models.CharField(max_length=100,blank=True,null=True)
    token=models.CharField(max_length=200,blank=True,null=True)
    def _str_(self):
        return self.first_name


# User details
class UserProfile(models.Model):
    CATEGORY_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('schoolpage', 'School Page'),
    ]
    
    EDUCATION_CHOICES = [
        ('school', 'School'),
        ('college', 'College'),
        ('institute', 'Institute'),
    ]
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    education_type = models.CharField(max_length=20, choices=EDUCATION_CHOICES, blank=True, null=True)

    def str(self):
        return self.username

class Student(UserProfile):
    college_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)

class Teacher(UserProfile):
    school_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)

class SchoolPage(UserProfile):
    founder_name = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)

class ourpartners(models.Model):
    PartnersName = models.CharField( max_length=100)
class SchoolDetails(models.Model):
    Schoolname = models.CharField( max_length=30)
    SchoolHeading = models.TextField()
    SchoolDescription = models.TextField()
class CollegeDetails(models.Model):
    Collegename = models.CharField( max_length=30)
    CollegeHeading = models.TextField()
    CollegeDescription = models.TextField()
class InstitutionDetails(models.Model):
    Institutionname = models.CharField( max_length=30)
    InstitutionHeading = models.TextField()
    InstitutionDescription = models.TextField()
    # portfolio of teachers
class InstructorportfolioItem(models.Model):
    image = models.ImageField(upload_to='portfolio_items/')
    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50)
    achievements_and_certificates = models.TextField(blank=True,null=True)
    field_of_expertise = models.CharField(max_length=50)
    connectedschool = models.IntegerField()
    connectedcollege = models.IntegerField()

    description = models.TextField(blank=True,null=True)
    abouts = models.TextField(blank=True,null=True)
    def _str_(self):
        return self.achievements_and_certificates
    
class CareerStrategiest(models.Model):
    postname= models.CharField(max_length=50)
    fieldname=models.CharField(max_length=50)
    officelocation = models.CharField(max_length=50)
    minimumqualification =models.CharField(max_length=50)
    experiencelavel = models.CharField(max_length=50)
    vacancylocation = models.CharField(max_length=30)
    jobdescription = models.TextField(max_length=100)
    technicalrequirement = models.TextField(max_length=200)
    type_choices = (
        ('school', 'School'),
        ('college', 'College'),
        ('institute', 'Institute'),
    )
    type = models.CharField(max_length=20, choices=type_choices, default='school')
    
    club_type_choices = (
        ('jobs', 'Jobs'),
        ('clubs', 'Clubs'),
    )
    club_type = models.CharField(max_length=20, choices=club_type_choices, default='jobs')

class AboutUs(models.Model):
    aboutus_descriptions = models.TextField(max_length=1000)
    photos = models.ImageField(max_length=50)


class CareerCounselors(models.Model):
    CollegeAndCareerCounselors=models.TextField(max_length=500)
    CollegeVineCounselors=models.TextField(max_length=1000)

class ClubDetails(models.Model):
    club_name=models.CharField(max_length=100)
    founded_year=models.IntegerField(max_length=4)
    full_name=models.CharField(max_length=50)
    total_registered_users=models.BigIntegerField()
    total_seats=models.BigIntegerField()
    total_applied_applications=models.BigIntegerField()
    remaining_seats=models.BigIntegerField()
    connectd_schools=models.IntegerField()
    connected_colleges=models.IntegerField()
    members=models.IntegerField()
    club_details=models.TextField(max_length=10000)
    aboutus=models.TextField(max_length=10000)
    photos = models.ImageField(upload_to='club_photogallery/')