from django.shortcuts import render

# Create your views here.
def app(request):

    context = {}
    return render(request, 'index.html', context)
