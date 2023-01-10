from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Какой же я молодец!!!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
