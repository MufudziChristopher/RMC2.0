from django.shortcuts import render

# Create your views here.
def RMC(request):

    context = {}
    return render(request, 'RMC.html', context)
