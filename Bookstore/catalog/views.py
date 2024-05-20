from django.shortcuts import render

from .models import Section, Category, Book
# Create your views here.

def mainpage(request):

    sections = Section.objects.all()
    data = {
        'sections': sections
    }
    return render(request,"index.html", data)



def sections(request, section_name):
    try:
        section = Section.objects.get(slug=section_name)
        categories = section.category_set.all()

        data = {
           'title': section.title,
            'categories': categories
        }
        return render(request, "sections.html", context=data)

    except:
        return render(request, "pageNotFound404.html", status=404)


def show_book(request):
    pass
def show_books(request, cat_name):
    category = Category.objects.get(slug=cat_name)
    results = Book.objects.filter(category=category.id)
    data = {
        'category': category.title,
        "products": results
    }
    return render(request, "books.html", context=data)


