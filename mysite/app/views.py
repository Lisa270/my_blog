from django.shortcuts import render

def post_list(request):
    return render(request, 'app/post_list.html', {})