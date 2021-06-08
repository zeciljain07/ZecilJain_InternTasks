from django.shortcuts import render

def homepageview(request):
    return render(request,'home.html')

def process(request):
    print(request.POST)
    a=(request.POST['name'])
    b=(request.POST['email'])
    c=(request.POST['birthday'])
    d=(request.POST['mob_no.'])
    e=(request.POST['password'])
    return render(request,'feedback.html',{'mya':a, 'myb':b, 'myc':c,'myd':d,'mye':e})