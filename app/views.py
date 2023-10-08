from django.shortcuts import render

# Create your views here.
#  defined a view function named home(). When calling this function, it’ll render an HTML file named home.html.
def home(request):
    return render(request, 'app/home.html', {})