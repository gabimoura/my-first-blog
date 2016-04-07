from django.shortcuts import render

def post_list(request):
    return render(request, 'tbreak/templates/tbreak/post_list.html', {})
