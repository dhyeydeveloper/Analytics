from django.shortcuts import render
from accounts.models import *
from trackingmodel.models import BitcoinTracking
from django.http import JsonResponse
import calendar
from django.db.models import F
from django.db.models.functions import TruncDay
from datetime import datetime
import json
# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def home_profile_func(request):
    users_data = UserProfile.objects.all()
    bitcoin_fetch_data = BitcoinTracking.objects.all().annotate(time_since_create=models.ExpressionWrapper((F('mytimestamp') - datetime(1970,1,1)), output_field=models.IntegerField())).values_list("time_since_create","price")
    bitcoin_data = [[x[0]/1000,x[1]] for x in bitcoin_fetch_data]
    context = {"users_data":users_data, "bitcoin_data":bitcoin_data}
    return render(request, "accounts/index.html", context)

def user_update_func(request, id):
    if is_ajax(request):    
        check_user = UserProfile.objects.filter(id= id)
        id = str(id)
        if check_user.exists():
            name, position, office, age, salary = request.POST.get("name"+id, None), request.POST.get("position"+id, None), request.POST.get("office"+id, None), request.POST.get("age"+id, None), request.POST.get("salary"+id, None)
            check_user.update(name=name, position=position, office=office, age=age, salary=salary)
            return JsonResponse({"status":"success","message":"User credentials updated."})
        return JsonResponse({"status":"failure","message":"User not found with given id."})

def user_delete_func(request, id):
    if is_ajax(request):    
        check_user = UserProfile.objects.filter(id= id)
        id = str(id)
        if check_user.exists():
            check_user.delete()     
            return JsonResponse({"status":"success","message":"User credentials deleted."})
        return JsonResponse({"status":"failure","message":"User not found with given id."})


# ============================================ FIREBASE NOTIFICATION CHANGES =====================================
from django.http import HttpResponse
import requests
def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyC9sG9ZqrCdBXfheywxdhQjkH-Iqajbc98",' \
         '        authDomain: "analytics-4a17d.firebaseapp.com",' \
         '        projectId: "analytics-4a17d",' \
         '        storageBucket: "analytics-4a17d.appspot.com",' \
         '        messagingSenderId: "916153433383",' \
         '        appId: "1:916153433383:web:30bad1d5acbf22344b7d02",' \
         '        measurementId: "G-N2XBMP70VK"' \
         ' };' \
         'firebase.initializeApp();' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")


def send_notification(registration_ids , message_title , message_desc):
    fcm_api = "AAAA1U7__Sc:APA91bGuYx72gOWuHhITHSSTPyX2nuZPaXnuZ70MZhPy6V8T4K2Auk99FDTvIyQKD8kKAf9cN4PZKkK6y336pjVkZkbKz4RiiPwPB8CLn4qxJKhMa6LF6-NuS6Oqsp12gQ0BGf3vXX3P"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
            "image" : "",
            "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())

import firebase_admin
from firebase_admin import credentials
def send(request):
    if not firebase_admin._apps:
        cred = credentials.Certificate("service-account-file.json")
        firebase_admin.initialize_app(cred)
    resgistration = ["fOzVdorYQKV1FPt8_03ain:APA91bHHqS7OZX_0MbfZ-GaVhFlO18E4LBihLbhmXS6LY2FwY72wcUWUFP2zaaVgRVMKWja1pjHaZwR0sjGX1hKi4xLCXI8jw1m0JKU3cFnsYnbfE-0cloCHJNl7mXiL1ZmYMud_SPwO"]
    send_notification(resgistration , 'Play Store' , "Today is Dhyey Mehta's birthday. Wish him.")
    return HttpResponse("sent")