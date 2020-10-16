from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    if request.method == "POST":
        return render(request, 'netmedsapp/index.html')
    return render(request, 'netmedsapp/index.html')
