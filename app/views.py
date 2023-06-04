from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'name':'halima','age':23}
    return render (request,'sample.html',context=d)