from django.shortcuts import render, redirect
from weather_api.key import api_key
import requests
import math
# from .models import Social

# Create your views here.

def index(request):
    return render(request, "weather_api/home.html")




def result(request):
    if request.method == "POST":
        city_name = request.POST["city"].lower()
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
        w_dataset = requests.get(url).json()
        try:
            context = {
                ####
                "city_name":w_dataset["city"]["name"],
                "city_country":w_dataset["city"]["country"],
                "wind":w_dataset['list'][0]['wind']['speed'],
                "degree":w_dataset['list'][0]['wind']['deg'],
                "status":w_dataset['list'][0]['weather'][0]['description'],
                "cloud":w_dataset['list'][0]['clouds']['all'],
                'date':w_dataset['list'][0]["dt_txt"],
                'date1':w_dataset['list'][1]["dt_txt"],
                'date2':w_dataset['list'][2]["dt_txt"],
                'date3':w_dataset['list'][3]["dt_txt"],
                'date4':w_dataset['list'][4]["dt_txt"],
                'date5':w_dataset['list'][5]["dt_txt"],
                'date6':w_dataset['list'][6]["dt_txt"],


                "temp": round(w_dataset["list"][0]["main"]["temp"] -273.0),
                "temp_min1":math.floor(w_dataset["list"][1]["main"]["temp_min"] -273.0),
                "temp_max1": math.ceil(w_dataset["list"][1]["main"]["temp_max"] -273.0),
                "temp_min2":math.floor(w_dataset["list"][2]["main"]["temp_min"] -273.0),
                "temp_max2": math.ceil(w_dataset["list"][2]["main"]["temp_max"] -273.0),
                "temp_min3":math.floor(w_dataset["list"][3]["main"]["temp_min"] -273.0),
                "temp_max3": math.ceil(w_dataset["list"][3]["main"]["temp_max"] -273.0),
                "temp_min4":math.floor(w_dataset["list"][4]["main"]["temp_min"] -273.0),
                "temp_max4": math.ceil(w_dataset["list"][4]["main"]["temp_max"] -273.0),
                "temp_min5":math.floor(w_dataset["list"][5]["main"]["temp_min"] -273.0),
                "temp_max5": math.ceil(w_dataset["list"][5]["main"]["temp_max"] -273.0),
                "temp_min6":math.floor(w_dataset["list"][6]["main"]["temp_min"] -273.0),
                "temp_max6": math.ceil(w_dataset["list"][6]["main"]["temp_max"] -273.0),


                "pressure":w_dataset["list"][0]["main"]["pressure"],
                "humidity":w_dataset["list"][0]["main"]["humidity"],
                "sea_level":w_dataset["list"][0]["main"]["sea_level"],


                "weather":w_dataset["list"][1]["weather"][0]["main"],
                "description":w_dataset["list"][1]["weather"][0]["description"],
                "icon":w_dataset["list"][0]["weather"][0]["icon"],
                "icon1":w_dataset["list"][1]["weather"][0]["icon"],
                "icon2":w_dataset["list"][2]["weather"][0]["icon"],
                "icon3":w_dataset["list"][3]["weather"][0]["icon"],
                "icon4":w_dataset["list"][4]["weather"][0]["icon"],
                "icon5":w_dataset["list"][5]["weather"][0]["icon"],
                "icon6":w_dataset["list"][6]["weather"][0]["icon"],

            }
        except:
            context = {

            "city_name":"Not Found, Check your spelling..."
        }

        return render(request, "weather_api/results.html", context)
    else:
    	return redirect('home')


import requests
from django.contrib import messages

def send_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        api_url = "https://ooklf83w6g.execute-api.eu-west-1.amazonaws.com/WeatherStage"
        data = {
            "email": email,
            "subject": "Test",
            "content": "Hello from WeatherPredic! Thank you for subscribing."
        }

        try:
            response = requests.post(api_url, json=data)
            if response.status_code == 200:
                messages.success(request, "Email sent successfully!")
            else:
                messages.error(request, "Failed to send email.")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")

    return redirect('home')

# Activity prediction API 
import requests
from django.shortcuts import render

def weather_with_activities(request):
    result = None
    if request.method == 'POST':
        country = request.POST.get('country')
        api_url = "https://65wb2cfcug.execute-api.eu-west-1.amazonaws.com/hproduction/suggest-activities?weather_condition="  # 👈 Your Lambda URL here

        try:
            response = requests.get(api_url, params={'country': country})
            if response.status_code == 200:
                result = response.json()
            else:
                result = {'error': f"API error: {response.status_code}"}
        except Exception as e:
            result = {'error': str(e)}

    return render(request, 'home.html', {'result': result})



# def social_links(request):
#     sl = Social.objects.all()
#     context = {
#         'sl': sl
#     }
#     return render(request, 'weather_api/base.html', context)

# import requests
# from django.shortcuts import redirect
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib import messages

# @csrf_exempt
# def send_email(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         subject = "Test"
#         content = "Hello, thank you for subscribing to Weather Predic!"

#         api_url = "https://ooklf83w6g.execute-api.eu-west-1.amazonaws.com/WeatherStage"
#         headers = {'Content-Type': 'application/json'}
#         payload = {
#             "email": email,
#             "subject": subject,
#             "content": content
#         }

#         try:
#             response = requests.post(api_url, json=payload, headers=headers)
#             if response.status_code == 200:
#                 messages.success(request, "Email sent successfully! Thank you for the subscrib.")
#             else:
#                 messages.error(request, f"Failed to send email. Status: {response.status_code}")
#         except Exception as e:
#             messages.error(request, f"Error: {str(e)}")

#     return redirect('home')  # redirect to your homepage or confirmation page
