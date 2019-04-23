from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.http import JsonResponse
# Create your views here.
import json
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def tnp_api_json(request):
    links_json = request.body
    links_tnp = json.loads(links_json)


    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('praveen.json', scope)
    client = gspread.authorize(creds)
    sht = client.open('TnP').sheet1
    links = []
    count = []
    for i in list(range(16,50)):
        l = sht.cell(i, 1).value
        if(l[6:] in links_tnp):
            links.append(l[6:])
            l = int(sht.cell(i, 2).value)
            count.append(l)

    b=len(links)
    for i in list(range(0,b-1)):
        max = i
        j = i + 1
        while (j < b):
            if (count[max] < count[j]):
                max = j
            j = j + 1
        a = links[max]
        links[max] = links[i]
        links[i] = a
        a = count[max]
        count[max] = count[i]
        count[i] = a
    print(links)
    print(count)

    for i in links_tnp:
        if(i not in links):
            links.append(i)
    name_json = json.dumps(links)
    print(name_json)
    k = JsonResponse(name_json, safe=False)
    return k
    #render(request, 'pageviews.html',locals())

def index(request):
    return render(request,'index.html')

def page(request):
    total = ['Link1','Link2','Link3','Link4','Link5']
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('praveen.json', scope)
    client = gspread.authorize(creds)
    sht = client.open('Majorprojectnew').sheet1
    links = []
    count =  []
    for i in list(range(16, 25)):
        l = sht.cell(i, 1).value
        if(l[7:11]=='link'):
            links.append(l)
            l = int(sht.cell(i, 2).value)
            count.append(l)
    b=len(links)
    for i in list(range(0,b-1)):
        max = i
        j = i + 1
        while (j < b):
            if (count[max] < count[j]):
                max = j
            j = j + 1
        a = links[max]
        links[max] = links[i]
        links[i] = a
        a = count[max]
        count[max] = count[i]
        count[i] = a
    print(links)
    print(count)
    name=[]
    for i in links:
        j=i[7:11]
        if(j=='link'):
            i=i[7:]
            i = i.title()
            name.append(i)
    print(name)
    for i in total:
        if(i not in name):
            name.append(i)

    print(name)
    dict={
          'n':name}


    return render(request, 'pageviews.html',{'dict':dict})
def link1(request):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('praveen.json', scope)
    client = gspread.authorize(creds)
    sht = client.open('Majorprojectnew').sheet1
    i=sht.cell(17,2).value
    dict={'l':i}
    return render(request, 'link1.html',{'dict':dict})
def link2(request):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('praveen.json', scope)
    client = gspread.authorize(creds)
    sht = client.open('Majorprojectnew').sheet1
    i=sht.cell(18,2).value
    dict={'l':i}
    return render(request, 'link2.html',{'dict':dict})
def link3(request):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('praveen.json', scope)
    client = gspread.authorize(creds)
    sht = client.open('Majorprojectnew').sheet1
    i=sht.cell(19,2).value
    dict={'l':i}
    return render(request, 'link3.html',{'dict':dict})
def link4(request):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('praveen.json', scope)
    client = gspread.authorize(creds)
    sht = client.open('Majorprojectnew').sheet1
    i=sht.cell(20,2).value

    dict={'l':i}
    return render(request, 'link4.html',{'dict':dict})
def link5(request):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('praveen.json', scope)
    client = gspread.authorize(creds)
    sht = client.open('Majorprojectnew').sheet1
    i=sht.cell(21,2).value
    dict={'l':i}
    return render(request, 'link5.html',{'dict':dict})
def average(request):
    total = ['Link1', 'Link2', 'Link3', 'Link4', 'Link5']
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('praveen.json', scope)
    client = gspread.authorize(creds)
    sht = client.open('Majorprojectnew').sheet1
    links = []
    count = []
    for i in list(range(16, 25)):
        l = sht.cell(i, 1).value
        if(l[7:11]=='link'):
            links.append(l)
            l = float(sht.cell(i, 3).value)
            count.append(l)
    b=len(links)
    for i in list(range(0, b-1)):
        max = i
        j = i + 1
        while (j < b):
            if (count[max] < count[j]):
                max = j
            j = j + 1
        a = links[max]
        links[max] = links[i]
        links[i] = a
        a = count[max]
        count[max] = count[i]
        count[i] = a
    print(links)
    print(count)
    name = []
    for i in links:
        j = i[7:11]
        if (j== 'link'):
            i=i[7: ]
            i = i.title()
            name.append(i)
    print(name)
    for i in total:
        if(i not in name):
            name.append(i)
    print(name)

    dict = {
        'n': name}

    return render(request, 'averagetime.html', {'dict': dict})

def product(request):
    total = ['Link1', 'Link2', 'Link3', 'Link4', 'Link5']
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('praveen.json', scope)
    client = gspread.authorize(creds)
    sht = client.open('Majorprojectnew').sheet1
    links = []
    count = []
    for i in list(range(16, 25)):
        l = sht.cell(i, 1).value
        if(l[7:11]=='link'):
            links.append(l)
            l = int(sht.cell(i, 2).value)
            m = float(sht.cell(i, 3).value)
            l=l*m
            count.append(l)

    b=len(links)
    for i in list(range(0, b-1)):
        max = i
        j = i + 1
        while (j < b):
            if (count[max] < count[j]):
                max = j
            j = j + 1
        a = links[max]
        links[max] = links[i]
        links[i] = a
        a = count[max]
        count[max] = count[i]
        count[i] = a
    print(links)
    print(count)
    name = []
    for i in links:
        j = i[7:11]
        if (j == 'link'):
            i=i[7: ]
            i = i.title()
            name.append(i)
    print(name)
    for i in total:
        if(i not in name):
            name.append(i)

    print(name)

    dict = {
        'n': name}

    return render(request, 'product.html', {'dict': dict})
