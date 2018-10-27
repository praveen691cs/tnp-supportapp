from django.shortcuts import render
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Create your views here.
def index(request):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('praveen.json', scope)
    client = gspread.authorize(creds)
    sht = client.open('Majorprojectnew').sheet1
    links = []
    count = []
    for i in list(range(17, 22)):
        l = sht.cell(i, 1).value
        links.append(l)
        l = int(sht.cell(i, 2).value)
        count.append(l)

    for i in list(range(0, 4)):
        max = i
        j = i + 1
        while (j < 5):
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
        i=i[7:]
        i=i.title()
        name.append(i)
    print(name)

    dict={
          'n':name}


    return render(request, 'index.html',{'dict':dict})
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