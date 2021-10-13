from django.shortcuts import render,redirect
from . models import Contact

# Create your views here.

def home(request):
    context = {}
    return render(request, 'index.html', context)

def event(request):
    context = {}
    return render(request, 'events.html', context)

def aboutus(request):
    context = {}
    return render(request, 'about-us.html', context)

def contactus(request):
    context = {}
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        cont=Contact(name=name,email=email,phone=phone,message=message)
        cont.save()
        return redirect('thank_you')
    return render(request, 'contact-us.html', context)

def gallery(request):
    context = {}
    return render(request, 'gallery.html', context)

def pooja(request):
    context = {}
    return render(request, 'pooja.html', context)

def ved(request):
    context = {}
    return render(request, 'ved.html', context)

def puran(request):
    context = {}
    return render(request, 'puran.html', context)

def upnishads(request):
    context = {}
    return render(request, 'Upnishads.html', context)

def geeta(request):
    context = {}
    return render(request, 'geeta.html', context)

def ramcharitmanas(request):
    context = {}
    return render(request, 'Ramcharitmanas.html', context)

def god(request):
    context = {}
    return render(request, 'god.html', context)

def goddess(request):
    context = {}
    return render(request, 'goddess.html', context)

def naugrah(request):
    context = {}
    return render(request, 'naugrah.html', context)

def final_design(request):
    context = {}
    return render(request, 'final_design.html', context)

def bhoomi_poojan(request):
    context = {}
    return render(request, 'bhoomi_poojan.html', context)

def stage10(request):
    context = {}
    return render(request, 'stage10.html', context)

def stage9(request):
    context = {}
    return render(request, 'stage9.html', context)

def stage8(request):
    context = {}
    return render(request, 'stage8.html', context)


def stage7(request):
    context = {}
    return render(request, 'stage7.html', context)

def stage6(request):
    context = {}
    return render(request, 'stage6.html', context)

def stage5(request):
    context = {}
    return render(request, 'stage5.html', context)

def stage4(request):
    context = {}
    return render(request, 'stage4.html', context)

def stage3(request):
    context = {}
    return render(request, 'stage3.html', context)

def stage2(request):
    context = {}
    return render(request, 'stage2.html', context)

def stage1(request):
    context = {}
    return render(request, 'stage1.html', context)

def thank_you(request):
    context = {}
    return render(request, 'thank_you.html', context)
    
def aarti(request):
    context = {}
    return render(request, 'aarti.html', context)

def chalisa(request):
    context = {}
    return render(request, 'chalisa.html', context)

def mantra(request):
    context = {}
    return render(request, 'mantra.html', context)

def aarti_shanidevji(request):
    context = {}
    return render(request, 'aarti-shanidev.html', context)

def aarti_ganeshji(request):
    context = {}
    return render(request, 'aarti-ganeshji.html', context)

def aarti_krishnaji(request):
    context = {}
    return render(request, 'aarti-krishna.html', context)

def aarti_laxmiji(request):
    context = {}
    return render(request, 'aarti-laxmiji.html', context)

def aarti_ramayanji(request):
    context = {}
    return render(request, 'aarti-ramayanji.html', context)

def aarti_durgaji(request):
    context = {}
    return render(request, 'aarti-durgaji.html', context)

def aarti_ramji(request):
    context = {}
    return render(request, 'aarti-ramji.html', context)

def aarti_vishnuji(request):
    context = {}
    return render(request, 'aarti-vishnuji.html', context)

def aarti_saraswatiji(request):
    context = {}
    return render(request, 'aarti-Saraswatiji.html', context)

def aarti_hanumanji(request):
    context = {}
    return render(request, 'aarti-hanumanji.html', context)

def aarti_shivji(request):
    context = {}
    return render(request, 'aarti-shivji.html', context)

def aarti_kaliji(request):
    context = {}
    return render(request, 'aarti-kaliji.html', context)