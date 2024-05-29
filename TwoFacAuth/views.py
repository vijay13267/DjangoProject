import logging
from datetime import datetime

import geocoder
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from djangoProject1.settings import EMAIL_HOST_USER
from django.conf import settings
from django.contrib import messages
from TwoFacAuth.forms import EmailForm
# from .models import OTP
# from .forms import EmailForm
import random
logger = logging.getLogger(__name__)

# def send_email():
#     send_mail(
#         'OTP Verification',
#         f'Your OTP is: 5555',
#         settings.EMAIL_HOST_USER,
#         # [email],
#         ["thesalvatore@careallianz.com"],
#         fail_silently=False,
#     )
#     return HttpResponse('OTP Verification')

def home(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        request.session['email'] = email
        request.session['otp'] = otp
        try:
            send_mail(
                'OTP Verification',
                f'Your OTP is: {otp}',
                settings.EMAIL_HOST_USER,
                # [email],
                [email],
                fail_silently=False,
            )
        except Exception as e:
            # Log the error message
            logger.error(f"Error sending OTP email: {e}")
            # Optionally, you can display a message to the user or redirect to an error page
            return HttpResponse("An error occurred while sending the OTP email. Please try again later.")
        return redirect('verify_otp')
    return render(request, 'home.html')

def verify_otp(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        email = request.session.get('email')
        otp = request.session.get('otp')
        if otp == otp_entered:
            messages.success(request, 'OTP verified successfully!')
            # Clear the session data after successful verification
            del request.session['email']
            del request.session['otp']
        else:
            messages.error(request, 'Invalid OTP, please try again.')
        return redirect('home')
    return render(request, 'verify_otp.html')

def temp_here(request):
    location = geocoder.ip('me').latlng
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
    now = datetime.now()
    hour = now.hour
    meteo_data = requests.get(api_request).json()
    temp = meteo_data['hourly']['temperature_2m'][hour]
    template = loader.get_template('index.html')
    context = {'temp': temp}
    # return HttpResponse(f"Here it's {temp}")
    return HttpResponse(template.render(context, request))

