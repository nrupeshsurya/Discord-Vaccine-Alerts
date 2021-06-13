import requests
from datetime import date
import time
from requests.models import Response


def get_appointment_session(pincode):
    today= date.today()
    d1 = today.strftime("%d-%m-%Y")
    print(d1)
    print(pincode)
    headers1={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51"}
    response = requests.get(url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+str(pincode)+"&date="+d1,headers=headers1)
    # response= requests.get(url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+pincode+'&date='+d1,headers=headers1)
    
    print(response)
    if response.status_code==200:
        data = response.json()
        hospital_data=[]
        if len(data['centers'])==0:
            return "No Available Data for this district"
        for i in data['centers']:
            temp_hosp=[]
            temp_hosp.append(i['name'])
            for k in i['sessions']:
                temp_hosp.append(k['available_capacity_dose1'])
                temp_hosp.append(k['date'])
                temp_hosp.append(k['slots'])
            if (temp_hosp[1]>0):
                hospital_data.append(temp_hosp)
    
        #print(hospital_data)
        to_return=""
        for i in hospital_data:
            stri=f'Hospital Name:{i[0]}\nAvailable Capacity:{i[1]}\nDate:{i[2]}\nAvailable Slots:{i[3]}\n\n'
            to_return+=stri
        print(len(to_return))    
        # print(type(to_return))
        return to_return
    return 'error'

discord_webhook_url = "https://discord.com/api/webhooks/853550796204933121/CWv9pwXtmL8W_iocPyia2Di_PTg-yBoll951tE3AQtd25FkVrMm_bmisNf3UYZn6Xg1L"

def web_hooks(delay):
    response = get_appointment_session(641402)
    if(len(response)>0):
        message = "<@428583398966165504>\n"+response
        data = {"content" : message}
        r = requests.post(discord_webhook_url,data=data)
    time.sleep(delay)
    web_hooks(delay)

web_hooks(60)