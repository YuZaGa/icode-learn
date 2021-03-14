from django.shortcuts import render


def dashboard(request): 
      
    # render function takes argument  - request 
    # and return HTML as response 
    return render(request, "ada-dashboard.html") 