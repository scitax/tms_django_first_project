from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# task 19.04
def comment_refactor(request):
    name = request.GET.get('name')
    _check_age(request.GET.get('age'))
    comment = request.GET.get('comment')
    if name and comment:
        message = ''
        comment_lines = [f'{line} (c) {name}' for line in comment.split('\n')]
        for line in comment_lines:
            message += line
        return HttpResponse(message)
    else:
        return HttpResponse('Hi')


def _check_age(age):
    try:
        if not age:
            return None
        if 0 < int(age) < 150:
            return age
    except ValueError:
        return HttpResponse(f'Wrong ange input: {age}. Int expected')


# task 19.5-19.6
def request_show_name(request, *args, **kwargs):
    name = request.GET.get('name')
    if name:
        return render(request, 'django_name_template.html', {'name': name})
    return render(request, 'form_template.html')

