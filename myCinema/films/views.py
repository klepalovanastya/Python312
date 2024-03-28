from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,"main_page.html")


def page_about_film(request, film_id):
    if film_id == 1:
        return render(request, "film1.html", {"article_number": film_id})
    elif film_id == 2:
        return render(request, "film2.html", {"article_number": film_id})
    elif film_id == 3:
        return render(request, "film3.html", {"article_number": film_id})

    return render(request, "pageNotFound404.html", status=404)