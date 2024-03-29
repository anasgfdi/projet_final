from django.shortcuts import render
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
import requests 

import pandas as pd 


# df = pd.read_csv('data_1.csv')



# def accueil(request):

#     return render(request,'home_page.html')
def api(request):

    headers = {'accept' : 'application/json','Content-Type': 'application/json'}
    quest = forms.PredictionForm


    if request.method == 'POST':
        form=quest(request.POST or None)

        if form.is_valid() :
            url = 'http://127.0.0.1:8003/predict'

            res = form.cleaned_data 
            print(form.cleaned_data)
            conversion = json.dumps(res)
            info= requests.post(url = url,data = conversion,headers=headers)
            raw_result = info.text
            print(raw_result)
            print(type(raw_result))
            result = None
            if raw_result == '0':
                result = 'Félicitations votre prêt a été accordé !'
            elif raw_result == '1':
                result = "Malheureusement votre dossier n'a pas été retenu , une prochaine fois peut-être ;)" 

            return render(request,"result.html",{"result":result})
            
    else:


        return render(request, "homepage.html", {'form':quest})

