from django.shortcuts import render, redirect , HttpResponseRedirect
from django.contrib.auth.hashers import make_password , check_password
from .models import Patient
from django.views import View
import random
from .middlewares.auth import auth_middleware
from django.contrib import messages



class Index(View):
    def get(self, request):
        # print()
        return render(request , 'index.html')


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        if len(request.FILES) != 0:
            image = request.FILES['image']
        username = postData.get('username')
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        DorP = postData.get('DorP')
        line1 = postData.get('line1')
        state = postData.get('state')
        city = postData.get('city')
        pincode = postData.get('pincode')
        password = postData.get('password')
        cpassword = postData.get('cpassword')
        # validation
        value = {
            'image': image,
            'username':username,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'DorP':DorP,
            'line1':line1,
            'state':state,
            'city':city,
            'pincode':pincode,
            'password':password,
            'cpassword':cpassword
        }
        error_message = None

        patient = Patient(image=image,
                            username=username,
                            first_name=first_name,
                            last_name=last_name,
                            email=email,
                            DorP=DorP,
                            line1=line1,
                            state=state,
                            city=city,
                            pincode=pincode,
                            password=password,
                            cpassword=cpassword)

        error_message = self.validatePatient(patient)

        if not error_message:
            print("checkinggggggggggggggg",image , first_name, last_name, email, password)
            patient.password = make_password(patient.password)
            patient.register()
            messages.success(request, 'Account has been created successfully')
            return redirect('loginPatient')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validatePatient(self, patient):
        error_message = None;
        if (not patient.first_name):
            error_message = "First Name Required !!"
        elif len(patient.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not patient.last_name:
            error_message = 'Last Name Required'
        elif len(patient.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif len(patient.password) < 6:
            error_message = 'Password must be 6 char long'
        elif not (patient.password == patient.cpassword):
            error_message = 'Two passwords do not match'
        elif len(patient.email) < 5:
            error_message = 'Email must be 5 char long'
        elif not patient.username.isalnum():
            error_message = 'Username should only contain alphabet and number'
        elif patient.isExists():
            error_message = 'Email Address Already Registered..'
        elif patient.isExistsByUsername():
            error_message = 'Username Already Registered..'
        # saving

        return error_message


class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        patient = Patient.get_patient_by_email(email)
        error_message = None
        if patient:
            flag = check_password(password, patient.password)
            if flag:
                request.session['patient'] = patient.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    if patient.DorP == '1':
                        messages.success(request, 'Logged In successfully')
                        return redirect('patient' , patient.id)
                    else:
                        messages.success(request, 'Logged In successfully')
                        return redirect('doctor', patient.id)
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)

        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    messages.success(request, 'Logged out successfully')
    return redirect('loginPatient')

@auth_middleware
def patient(request, id):
    pord = Patient.objects.filter(id=id)
    return redirect('profile' , id)

@auth_middleware
def doctor(request, id):
    doc = Patient.objects.filter(id=id).first()
    temp = Patient.objects.filter(DorP='1')
    end = len(temp)-3
    print(len(temp))
    new_patients = Patient.objects.filter(DorP='1').order_by('-id')[:3]
    recent = Patient.objects.filter(DorP='1').order_by('id')[:end]
    print(doc, recent , new_patients )
    return render(request, 'doctor.html', {'doc':doc , 'new_patients':new_patients , 'recent':recent})

@auth_middleware
def profile(request,id):
    person = Patient.objects.filter(id=id).first()
    doctors = Patient.objects.filter(DorP='2')
    print(len(doctors)-3)
    ran = random.randint(0, len(doctors))
    return render(request, 'profile.html', {'ran':ran, 'doctors':doctors , 'person':person })