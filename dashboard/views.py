from django.shortcuts import render
from django.http import HttpResponse

from dashboard.models import MarqueeText

# Create your views here.

def index(request):
    marquee_text = MarqueeText.objects.first()
    return render(request, 'dashboard/index.html', {'marquee_text': marquee_text})

def staff(request):
    return render(request, 'dashboard/staff.html')

def admin(request):
    return render(request, 'admin.html')