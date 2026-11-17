from django.shortcuts import render

# Create your views here.


# success page view

def success_view(request):
    return render(
        request,
        template_name='successful.html'
    )