from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        "title": "Home",
        "contributor": "Bean",
        "nav": [["", "Blog"], ["recent/", "Recent post"]],
    }
    return render(request, "blog/index.html", data)


def recent(request):
    data = {"title": "Recent Post", "contributor": "Bean"}
    return render(request, "blog/recent.html", data)
