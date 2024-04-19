from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from .models import Books, Tasks
from my_app.forms import *

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

def page_books(request):
    if request.method == 'POST':
        title_book = request.POST.get('book')
        Books.objects.create(title=title_book)
        return HttpResponse(f"""
<h2>Новая книга успешно добавлена</h2>
<a href=""><button>Вернуться на страницу с книгами</button></a>""")
    elif request.method == 'GET':
        results = Books.objects.all()
        data = {
            "book": results
        }
        return render(request, "books.html", data)


def page_editBook(request):
    results = Books.objects.all()
    data = {
        "book": results
    }
    return render(request, "books.html", data)

def page_tasks(request):
    if request.method == 'POST':
        # title_task = request.POST.get('title')
        # description_task = request.POST.get('description')
        # status_task = request.POST.get('status')
        # Tasks.objects.create(title=title_task, description=description_task, status=status_task)
        form = AddTaskForm(request.POST)
        form.save()
        return HttpResponse(f"""
        <h2>Новое задание успешно добавлено</h2>
        <a href=""><button>Вернуться на страницу с задачами</button></a>""")
    elif request.method == 'GET':
        results = Tasks.objects.all()
        data = {
            "task": results,
            'add_task_form': AddTaskForm()
        }
        return render(request, "tasks.html", data)

def page_editTask(request, task_id):
    taskData = Tasks.objects.get(id=task_id)
    if request.method == "GET":
        data = {"id": task_id,
                "text": taskData.title,
                "description": taskData.description,
                "status": taskData.status,
                "date_created": taskData.date_created,
                'add_task_form': AddTaskForm()
                }
        return render(request, 'editTask.html', data)

    # ------------------- UPDATE ---------------------#
    if request.method == 'POST':
        taskData.title = request.POST.get('title')
        taskData.description = request.POST.get('description')
        taskData.status = request.POST.get('description')
        taskData.save()
        return HttpResponseRedirect("../../tasks/")

def page_deleteTask(request, task_id):
    try:
        task = Tasks.objects.get(id=task_id).delete()
        return HttpResponseRedirect("../../tasks/")
    except Tasks.DoesNotExist:
        return HttpResponseNotFound("""<h2>Task not found</h2>
        <a href="../../tasks/"><button>Вернуться на страницу с задачами</button></a>""")











