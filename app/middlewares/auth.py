from django.shortcuts import redirect
from django.contrib import messages

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request ,*callback_args, **callback_kwargs):
        print("middleware",request.session.get('patient'))

        if not request.session.get('patient'):
            messages.error(request, 'Please login first')
            return redirect('loginPatient')

        response = get_response(request,*callback_args, **callback_kwargs)
        return response
    return middleware