from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def mainpage(request):
    return render(request,"mainpage.html")

def picture(request, picture_name_slug):
    if picture_name_slug == 'mona-liza':
        return render(request,"picture1.html")
    elif picture_name_slug == 'rozhdenie-venery':
        return render(request,"picture2.html")
    elif picture_name_slug == 'poslednij-den-pompei':
        return render(request,"picture3.html")
    return render(request, "pageNotFound404.html", status=404)

def products(request, product_id):
    if product_id == 1:
        return render(request, "product1.html", {"article_number": product_id})
    elif product_id == 2:
        return render(request, "product2.html", {"article_number": product_id})
    elif product_id == 3:
        return render(request, "product3.html", {"article_number": product_id})

    return render(request, "pageNotFound404.html", status=404)

def page_news(request):

    data = {"Лазарев опроверг информацию о завершении карьеры":"шоу-бизнес",
            "Игорь Николаев отреагировал на слухи о разводе с Юлией Проскуряновой":"шоу-бизнес",
            "'Ненормальный', 'Сказки Гофмана' и 'Летучий корабль': наше кино на экранах":"культура",
            "Режиссеру Кристоферу Нолану присвоят звание рыцаря":"культура",
            "Халили выиграл масс старт на чемпионате России по биатлону в Тюмени":"спорт",
            "Вратарь Федотов рассказал, как произошло его расставание с хоккейным ЦСКА":"спорт"}
    return render(request,"news.html", context={"data": data})
