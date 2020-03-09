from django.shortcuts import render


def login(request):
    return render(request, 'registration/login.html')





# def dashboard(request):
#     return render(request,'')