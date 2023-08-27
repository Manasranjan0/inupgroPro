"""inupgropro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from inupgroapp.views import ExperienceLevelFilterView, ClubTypeFilterView,FindJobViewSet,CollegeDetailsList, HostLogView, HostForgotPasswordView,HostChangePasswordView,collegeEducationCountView
from inupgroapp.views import user_registration,ClubDetails,CareerCounselors,AboutUs,CareerStrategiest,InstitutionDetailsList,UserProfileAndTeacherList,OurPartnersList,HostSignupView,SchoolDetailsList,AllTeacherData
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inupgroapp.views import FindJobViewSet
from inupgroapp import views
router = DefaultRouter()
router.register(r'jobs', FindJobViewSet,basename='job')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_details',user_registration.as_view(),name='user_details'),
    path('host_signup/', HostSignupView.as_view(), name='host_signup'),
    path('host_login/', HostLogView.as_view(), name='host_login'),
    path('host_forgot_password/', HostForgotPasswordView.as_view(), name='host_forgot_password'),
    path('host_change_password/', HostChangePasswordView.as_view(), name='host_change_password'),
    path('college_education-count/', collegeEducationCountView.as_view(), name='college_education_count'),
    path('api_schools/', SchoolDetailsList.as_view(), name='school_list'),
    path('api_colleges/', CollegeDetailsList.as_view(), name='college_list'),
    path('api_institutions/', InstitutionDetailsList.as_view(), name='institution_list'),
    path('api_OurPartnersList/',OurPartnersList.as_view(), name='api_OurPartnersList'),
    path('api/userprofiles_and_teachers/', UserProfileAndTeacherList.as_view(), name='userprofile_teacher_list'),
    path('api/UserProfileAndTeacherList/', AllTeacherData.as_view(), name='UserProfileAndTeacherList'),
    path('api/AboutUs/', AboutUs.as_view(), name='AboutUs'),
    path('api/CareerCounselors/', CareerCounselors.as_view(), name='CareerCounselors'),
    path('api/ClubDetails/', ClubDetails.as_view(), name='ClubDetails'),
    path('api/CareerStrategiest/', include(router.urls)),
    path('api_filtered/', ClubTypeFilterView.as_view(), name='club-type-filter'),
    path('api_filtered_by_experience/', ExperienceLevelFilterView.as_view(), name='experience-level-filter')
    # path('forgotpassword/', HostForgotPasswordView.as_view()),
    # path('changepassword/', HostChangePasswordView.as_view()),
]

# D:\My WORK\Projects\cms_project\web-inupgro-\inupgropro\manage.py