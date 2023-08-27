from rest_framework import serializers
from .models import ClubDetails,host_UserData,UserProfile,Student,Teacher,SchoolPage,AboutUs
from .models import SchoolDetails,CareerCounselors, CollegeDetails, InstitutionDetails,ourpartners,InstructorportfolioItem,CareerStrategiest

class UserProfileAndTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['firstname']

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class SchoolDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolDetails
        fields ='__all__'
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
class OurPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ourpartners
        fields='__all__'
class CollegeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeDetails
        fields = '__all__'

class InstitutionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstitutionDetails
        fields = '__all__'
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('firstname', 'lastname')

class InstructorportfolioItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstructorportfolioItem
        fields = '__all__'


class CareerStrategiestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerStrategiest
        fields = '__all__'
         
class CareerCounselorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerCounselors
        fields = '__all__'
         
class ClubDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubDetails
        fields = '__all__'
         