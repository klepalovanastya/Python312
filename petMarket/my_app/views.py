from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def mainpage(request):
    return HttpResponse("<h2>Произведения искусства<img src='https://instory.su/assets/covers/a28263df-4450-47cb-9fc8-becbef2d5d72.jpg'></h2>")

def picture(request, picture_name_slug):
    if picture_name_slug == 'mona-liza':
        return HttpResponse("<h2>Мона Лиза</h2>"
                     "<h3>Художник: Леонардо да Винчи</h3>"
                     "<h3>Описание: «Мона Лиза» (полное название — «Портрет госпожи Лизы дель Джокондо») — картина Леонардо да Винчи, одно из самых известных произведений живописи.Точная дата написания неизвестна (по некоторым сведениям, написана между 1503 и 1505 годами).На картине изображена Лиза Герардини, супруга флорентийского торговца шёлком Франческо дель Джокондо. </h3>"
                     "<h3>Цена: $970 млн.</h3>"
                     "<img src='https://img.championat.com/s/1350x900/news/big/u/w/mona-liza-s-nogami-nejroset-dopolnila-klassicheskie-kartiny_16544453091715239255.jpg'>"
                     )
    elif picture_name_slug == 'rozhdenie-venery':
        return HttpResponse("<h2>Рождение Венеры</h2>"
                            "<h3>Художник: Сандро Боттичелли</h3>"
                            "<h3>Описание: Картина итальянского художника флорентийской школы Сандро Боттичелли. Представляет собой живопись темперой на холсте размером 172,5 × 278,5 см. В настоящее время хранится в галерее Уффици, Флоренция. </h3>"
                            "<h3>Цена: $92,2 млн.</h3>"
                            "<img src='https://ae01.alicdn.com/kf/H13339de3fed945b8b478e0f62d9b07d6w/Sandro-Botticelli-The-Birth-of-Venus-Metal-Tin-Signs-12x8-Inch-Wall-Decor-Kitchen.jpg'>"
                            )
    elif picture_name_slug == 'poslednij-den-pompei':
        return HttpResponse("<h2>Последний день Помпеи</h2>"
                            "<h3>Художник: Карл Брюллов</h3>"
                            "<h3>Описание: «Последний день Помпеи» — крупноформатная картина русского художника Карла Брюллова (1799–1852), работа над которой была завершена в 1833 году.На картине изображены события в Помпеях во время катастрофического извержения Везувия, которое произошло в 79 году нашей эры.</h3>"
                            "<h3>Цена: 35000 - 40000 $.</h3>"
                            "<img src='https://img.goodfon.ru/original/4000x2788/b/3c/bryullov-posledniy-den-pompei.jpg'>"
                            )
    return HttpResponseNotFound("<h2>Страница не найдена</h2>")
