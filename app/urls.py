from django.urls import path
from .views import Signup , Index, Login , logout, patient, viewallpostbydoctor, allpostbycategory , doctor, patientpostview, profile, editpost, deletepost, addpost , fullview ,viewalldraftpost

urlpatterns = [
    path('', Signup.as_view(), name='signupPatient'),
    path('login', Login.as_view(), name='loginPatient'),
    path('logout', logout , name='logout'),
    path('patient/<int:id>', patient , name='patient'),
    path('doctor/<int:id>', doctor , name='doctor'),
    path('profile/<int:id>', profile , name='profile'),
    path('editpost/<int:postid>', editpost , name='editpost'),
    path('addpost', addpost , name='addpost'),
    path('deletepost/<int:postid>', deletepost , name='deletepost'),
    path('publishpost', patientpostview , name='patientpostview'),
    path('fullview/<slug:the_slug>', fullview , name='fullview'),
    path('viewdraftpost/<int:userid>', viewalldraftpost , name='draftpost'),
    path('viewallpostbydoctor', viewallpostbydoctor , name='viewallpostbydoctor'),
    path('catpost/<int:catid>', allpostbycategory , name='allpostbycategory'),

]


