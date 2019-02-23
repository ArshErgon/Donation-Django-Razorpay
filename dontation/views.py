
from django.shortcuts import render

from .forms import DonationForm

def charity_home(request):
    donation_form = DonationForm()
    name = request.POST.get("name")
    email = request.POST.get("email")
     # Rs1 = 100ps
    try:
        donation = int(request.POST.get("donation"))*100
    except TypeError:
        donation = 100
    message = request.POST.get("message")
    print(name, email, donation, message)
    print(type(donation))
    return render(request, 'index.html',{'name':name, 'email':email, 'donation':donation, 'message':message, "donation_form":donation_form})
