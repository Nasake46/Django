from django.shortcuts import render
from paste.models import Paste

def index(request):
    pastes = Paste.objects.all()
    return render(
        request, "paste/index.html",
        context={"pastes": pastes}
        )


def pasteview(request, url):
    un_paste = Paste.objects.get(url=url)
    return render(request, "paste/paste.html", context={"paste": un_paste})
