from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.response import Response
from django.views import View
from rest_framework.views import APIView
from inupgroapp.models import host_UserData
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import serializers
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import PropertySerializer
import jwt
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied
from django.conf import settings
import json
import re
from django.contrib.auth import get_user
from django.forms.models import model_to_dict
from django.shortcuts import render, HttpResponse
from .models import UserProfile, Student, Teacher, SchoolPage

from rest_framework import generics,status
from .models import ClubDetails,AboutUs,CareerCounselors,CareerStrategiest,SchoolDetails, CollegeDetails, InstitutionDetails,ourpartners,Teacher,UserProfile
from .serializers import  ClubDetailsSerializer,InstructorportfolioItemSerializer,InstructorportfolioItem,CareerCounselorsSerializer,AboutUsSerializer,CareerStrategiestSerializer,UserProfileSerializer,SchoolDetailsSerializer, CollegeDetailsSerializer, InstitutionDetailsSerializer,OurPartnersSerializer,UserProfileAndTeacherSerializer,TeacherSerializer






User = get_user_model()
@method_decorator(csrf_exempt, name='dispatch')
class HostSignupView(View):
    def post(self, request):
        jsonData = json.loads(request.body)
        first_name=jsonData.get('first_name')
        last_name=jsonData.get('last_name')
        email = jsonData.get('email')
        phone = jsonData.get('phone')
        password = jsonData.get('password')
        
         # Email verification
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return JsonResponse({'success': False, 'message': 'Invalid email format.'})
        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'email is already taken.'})
        # Phone verification
        # if not re.match(r"^[0-9]{10}$", phone):
        #     return JsonResponse({'success': False, 'message': 'Invalid phone number format.'})  
        # user_data = host_UserData(first_name=first_name,last_name=last_name, email=email, phone=phone, password=make_password(password))
        # user_data.save() 

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name=first_name
        user.last_name=last_name
        user.save()

        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'password':make_password(password),
        }
        login(request, user)
        payload = {'user_id': user.id}
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        return JsonResponse({'success': True, 'message': 'User created successfully.', 'data': data, 'token': str(token)},status=200)

@method_decorator(csrf_exempt, name='dispatch')
class HostLogView(View):
    def post(self, request):
        jsonData = json.loads(request.body)
        email = jsonData.get('email')
        password = jsonData.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # user_data = host_UserData.objects.get(email=email)
            # data = {
            #     'user_id': user.id,
            #     'first_name': user_data.first_name,
            #     'last_name': user_data.last_name,
            #     'email': user_data.email,
            #     'password': user_data.password,
            # }
            payload = {'user_id': user.id}
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
            return JsonResponse({'success': True,'token': str(token)},status=200)
        else:
            return JsonResponse({'success': False, 'error': 'Invalid login credentials'},status=401)

@method_decorator(csrf_exempt, name='dispatch')
class HostForgotPasswordView(View):
    def post(self, request):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            return render(request, 'change.html', {'email': email})
        else:
            messages.error(request, 'This email address does not exist.')
            return redirect('forgot_password')
@method_decorator(csrf_exempt, name='dispatch')
class HostChangePasswordView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'})

        if not email:
            return JsonResponse({'error': 'Email is required.'})
        elif not password:
            return JsonResponse({'error': 'Password is required.'})

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'error': 'No user with the given email exists.'})

        user.set_password(password)
        user.save()
        return JsonResponse({'success': 'Your password has been changed successfully.'},status=200)
    


    # user registration
class user_registration(APIView):
    serializer_class = UserProfileSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            category = serializer.validated_data['category']
            education_type = serializer.validated_data['education_type']
            
            if education_type == 'school':                    #for school id is 1
                if category == 'student':                     #for student id is 1.1
                    category_code = '1.1'               
                    education_type_code = '1'
                elif category == 'teacher':                    #for teacher id is 1.2
                    category_code = '1.2'
                    education_type_code = '1'
                elif category == 'schoolpage':                  #for school page id is 1.3
                    category_code = '1.3'
                    education_type_code = '1'
            elif education_type == 'college':                   #for college id is 2
                if category == 'student':                       #for school id is 2.1
                    category_code = '2.1'
                    education_type_code = '2'
                elif category == 'teacher':
                    category_code = '2.2'                       #for teacher id is 2.2
                    education_type_code = '2'
                elif category == 'schoolpage':
                    category_code = '2.3'                       #for school page id is 2.3
                    education_type_code = '2'
            elif education_type == 'institute':
                if category == 'student':
                    category_code = '3.1'
                    education_type_code = '3'
                elif category == 'teacher':
                    category_code = '3.2'
                    education_type_code = '3'
                elif category == 'schoolpage':
                    category_code = '3'
                    education_type_code = '3.3'
            
            serializer.save(category=category_code, education_type=education_type_code)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# total number of school college Teacher institute 
class collegeEducationCountView(View):
    def get(self, request, *args, **kwargs):
        college_count = UserProfile.objects.filter(education_type='college').count()
        institute_count = UserProfile.objects.filter(education_type='institute').count()
        teacher_count = UserProfile.objects.filter(category='teacher').count()

        response_data = {
            'college_education_count': college_count,
            'institute_count': institute_count,
            'teacher_count': teacher_count,
        }
        if college_count == 0 and institute_count == 0 and teacher_count == 0:
            response_data['message'] = 'No data available.'
            return JsonResponse(response_data, status=204)  # No Content
        else:
            return JsonResponse(response_data, status=200)

class SchoolDetailsList(generics.ListAPIView):
    queryset = SchoolDetails.objects.all()
    serializer_class = SchoolDetailsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'School details retrieved successfully',
            'data': serializer.data
        }
        return Response(data, status=200)


class CollegeDetailsList(generics.ListAPIView):
    queryset = CollegeDetails.objects.all()
    serializer_class = CollegeDetailsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'College details retrieved successfully',
            'data': serializer.data
        }
        return Response(data,status=200)

class InstitutionDetailsList(generics.ListAPIView):
    queryset = InstitutionDetails.objects.all()
    serializer_class = InstitutionDetailsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'Institution details retrieved successfully',
            'data': serializer.data
        }
        return Response(data,status=200)

class OurPartnersList(generics.ListAPIView):
    queryset=ourpartners.objects.all()
    serializer_class = OurPartnersSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'Partners retrieved successfully',
            'data': serializer.data
        }
        return Response(data,status=200)


class UserProfileAndTeacherList(APIView):
    def get(self, request, *args, **kwargs):
        teachers = Teacher.objects.all()
        teacher_data_list = []

        for teacher in teachers:
            user_profile = UserProfile.objects.filter(teacher=teacher).first()
            if user_profile:
                teacher_data = {
                    'first_name': user_profile.firstname,
                    'last_name': user_profile.lastname,
                    'school_name': teacher.school_name,
                    'subject': teacher.subject,
                    'experience': teacher.experience,
                }
                teacher_data_list.append(teacher_data)

        response_data = {
            'status': 'success',
            'message': 'Teacher details retrieved successfully',
            'data': teacher_data_list
        }

        return Response(response_data, status=200)

    
# All teacher data for video
class AllTeacherData(generics.ListAPIView):
    queryset=InstructorportfolioItem.objects.all()
    serializer_class = InstructorportfolioItemSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'All Teachers Data retrieved successfully',
            'data': serializer.data
        }
        return Response(data,status=200)


    
# Career Statery(Vacany related )
class CareerStrategiest(generics.ListAPIView):
    queryset=CareerStrategiest.objects.all()
    serializer_class = CareerStrategiestSerializer


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'Career Strategiest retrieved successfully',
            'data': serializer.data
        }
        return Response(data,status=200)
class AboutUs(generics.ListAPIView):
    queryset=AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'AboutUs Details retrieved successfully',
            'data': serializer.data
        }
        return Response(data,status=200)



# CareerCounselors

class CareerCounselors(generics.ListAPIView):
    queryset=CareerCounselors.objects.all()
    serializer_class = CareerCounselorsSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'Career Counselors Details retrieved successfully',
            'data': serializer.data
        }
        return Response(data,status=200)



#Club Details

class ClubDetails(generics.ListAPIView):
    queryset=ClubDetails.objects.all()
    serializer_class = ClubDetailsSerializer


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'status': 'success',
            'message': 'Club Details retrieved successfully',
            'data': serializer.data
        }
        return Response(data,status=200)












# class UserProfileAndTeacherList(APIView):
#     def get(self, request, *args, **kwargs):
#         combined_data = []

#         teacher_portfolio_items = TeacherPortfolioItem.objects.select_related('user_profile')
        
#         for portfolio_item in teacher_portfolio_items:
#             data = {
#                 'first_name': portfolio_item.user_profile.firstname,
#                 'last_name': portfolio_item.user_profile.lastname,
#                 'image': portfolio_item.image.url,
#                 'achievements_and_certificates': portfolio_item.achievements_and_certificates,
#                 'description': portfolio_item.description,
#                 'abouts': portfolio_item.abouts,
#             }
#             combined_data.append(data)
        
#         serializer = UserProfileAndTeacherList(combined_data, many=True)
#         return Response(serializer.data)





# def user_registration(request):
#     print("Form submitted!")  # Print to check if form submission reaches the view
#     if request.method == 'POST':
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         dob = request.POST.get('dob')
#         category = request.POST.get('category')
#         education_type = request.POST.get('education_type')

#         model_mapping = {
#             ('student', 'school'): Student,
#             ('teacher', 'school'): Teacher,
#             ('schoolpage', 'institute'): SchoolPage,
#         }

#         EducationModel = model_mapping.get((category, education_type))

#         if EducationModel:
#             try:
#                 if category == 'student':
#                     class_name = request.POST.get('class')
#                     school_name = request.POST.get('school')
#                     EducationModel.objects.create(
#                         firstname=firstname,
#                         lastname=lastname,
#                         username=username,
#                         email=email,
#                         phone=phone,
#                         dob=dob,
#                         education_type=education_type,
#                         category=category,
#                         college_name=class_name,
#                         school_name=school_name,
#                     )
#                 elif category == 'teacher':
#                     school_name = request.POST.get('school')
#                     subject = request.POST.get('subject')
#                     experience = request.POST.get('experience')
#                     EducationModel.objects.create(
#                         firstname=firstname,
#                         lastname=lastname,
#                         username=username,
#                         email=email,
#                         phone=phone,
#                         dob=dob,
#                         education_type=education_type,
#                         category=category,
#                         school_name=school_name,
#                         subject=subject,
#                         experience=experience,
#                     )
#                 elif category == 'schoolpage':
#                     founder_name = request.POST.get('founderYear')
#                     school_name = request.POST.get('schoolName')
#                     EducationModel.objects.create(
#                         firstname=firstname,
#                         lastname=lastname,
#                         username=username,
#                         email=email,
#                         phone=phone,
#                         dob=dob,
#                         education_type=education_type,
#                         category=category,
#                         founder_name=founder_name,
#                         school_name=school_name,
#                     )
#                 else:
#                     return HttpResponse('Invalid category')
                
#                 return HttpResponse('Data saved successfully')
#             except Exception as e:
#                 return HttpResponse(f'Error: {e}')
    
#     return render(request, 'school_info.html')


from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import CareerStrategiest
from .serializers import CareerStrategiestSerializer

class FindJobViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CareerStrategiestSerializer

    def get_queryset(self):
        type_filter = self.request.query_params.get('type', None)
        if type_filter:
            return CareerStrategiest.objects.filter(type=type_filter)
        return CareerStrategiest.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
class ClubTypeFilterView(View):
    def get(self, request, *args, **kwargs):
        club_type_filter = request.GET.get('club_type_filter', None)

        if club_type_filter:
            queryset = CareerStrategiest.objects.filter(club_type=club_type_filter)
        else:
            queryset = CareerStrategiest.objects.all()

        serializer = CareerStrategiestSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        return HttpResponse(status=405)
class ExperienceLevelFilterView(View):
    def get(self, request, *args, **kwargs):
        experience_range = request.GET.get('experience_range', None)
        queryset = CareerStrategiest.objects.all()

        if experience_range:
            min_experience, max_experience = map(int, experience_range.split('-'))
            queryset = queryset.filter(experiencelavel_gte=min_experience, experiencelavel_lt=max_experience)

        serializer = CareerStrategiestSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        return HttpResponse(status=405)