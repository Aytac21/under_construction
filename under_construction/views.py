from django.shortcuts import render

def under_construction_view(request):
    return render(request, 'index.html')