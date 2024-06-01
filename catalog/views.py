from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Section, Category, Book
from feedback.models import Feedback
# Create your views here.

# def mainpage(request):
#
#     sections = Section.objects.all()
#     data = {
#         'sections': sections
#     }
#     return render(request,"index.html", data)

class MainPage(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Главная страница',
                     # 'books': Book.objects.filter() в будущем на странице будут отображаться 3 избранные книги или новинки
    }

# def sections(request, section_name):
#     try:
#         section = Section.objects.get(slug=section_name)
#         categories = section.category_set.all()
#
#         data = {
#            'title': section.title,
#             'categories': categories
#         }
#         return render(request, "categories.html", context=data)
#
#     except:
#         return render(request, "pageNotFound404.html", status=404)


class Category(ListView):
    model = Category
    template_name = 'books.html'
    context_object_name = 'categories'  # 'products' - это ключ словаря

    def render_to_response(self, context, **response_kwargs):
        if context['error'] == 'error':
            return render(self.request, 'pageNotFound404.html',  context, **response_kwargs, status=404)
        return super().render_to_response(context, **response_kwargs)

    def get_context_data(self, **kwargs):
        # Дополнительные данные для передачи в контекст (необязательно)
        context = super().get_context_data(**kwargs)
        sections = Section.objects.all()
        try:
            section = Section.objects.get(slug=self.kwargs['slug'])
            categories = Category.objects.filter(section=section.id)
            books = Book.objects.filter(category=section.id)
            context['sections'] = sections
            context['section'] = section
            context['categories'] = categories
            context['books'] = books
            context['error'] = ''
        except:

            context['error'] = 'error'
        return context

# def show_books(request, cat_name):
#     category = Category.objects.get(slug=cat_name)
#     results = Book.objects.filter(category=category.id)
#     data = {
#         'category': category.title,
#         "products": results
#     }
#     return render(request, "catalog.html", context=data)

class Catalog(ListView):
    model = Book
    template_name = 'catalog.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = Section.objects.all()
        return context


# def show_book(request):
#     pass


class AboutBook(DetailView):
    model = Book
    template_name = 'book.html'
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = Book.objects.get(id=self.kwargs['product_id']) 
        feedbacks = book.feedback_set.all()
        context['feedbacks'] = feedbacks
        return context


