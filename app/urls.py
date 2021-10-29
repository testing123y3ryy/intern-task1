from django.urls import path
from .views import Signup , Index, Login , logout, patient , doctor, profile

urlpatterns = [
    path('', Signup.as_view(), name='signupPatient'),
    path('login', Login.as_view(), name='loginPatient'),
    path('logout', logout , name='logout'),
    path('patient/<int:id>', patient , name='patient'),
    path('doctor/<int:id>', doctor , name='doctor'),
    path('profile/<int:id>', profile , name='profile'),

]


