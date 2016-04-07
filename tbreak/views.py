from django.shortcuts import render

def post_list(request):
    return render(request, 'tbreak/post_list.html', {})
