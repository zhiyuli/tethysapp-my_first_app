from django.shortcuts import render


def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'my_first_app/home.html', context)