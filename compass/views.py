from django.shortcuts import render

def compass(request):

    return render(request, "status.html", {
        'heading': '99',
    })