from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .service import storage

def redirect(request: HttpRequest, id):
    return HttpResponseRedirect(storage.get_link(id))


def index(request: HttpRequest):
    return render(request, 'index.html')


def create_link(request: HttpRequest):
    link = request.POST.get('link')
    short = storage.add_link(link)
    return HttpResponse(f"<p>Ваша ссылка:</p><a target=\"_blank\" \
                        rel=\"noopener noreferrer\" \
                        href=http://localhost:8000/app/{short}>http://localhost:8000/app/{short}</a>")