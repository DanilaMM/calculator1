from django.shortcuts import render
from django.views import View

# Create your views here.
class Calculator(View):
    def post(self, request):
        coast = request.POST['cost']
        power = request.POST['power']
        cvt = request.POST['cvt']
        hours = request.POST['hours']
        minutes = request.POST['minutes']
        time = float(hours) + float(minutes)/60
        print(power, cvt, hours, minutes)
        if power=='kW':
            itog = float(coast)*float(cvt)*time
        else:
            itog = float(coast)*float(cvt)*time/1000

        itog = round(itog, 2)
        week = itog*7
        mounth = itog * 30
        year = itog * 365
        data = {
            'itog': itog,
            'week': week,
            'mounth': mounth,
            'year': year,
            'hours': hours,
            'minutes': minutes,
        }

        return render(request, 'calculate.html', context=data)

    def get(self, request):
        data = {
            'itog': None
        }
        return render(request, 'calculate.html')