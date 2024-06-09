from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Section, Category, Book
from feedback.models import Feedback
# Create your views here.

class MainPage(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Главная страница',
                     # 'books': Book.objects.filter() в будущем на странице будут отображаться 3 избранные книги или новинки
    }

class AboutUs(TemplateView):
    template_name = 'about_us.html'



class Sections(ListView):
    model = Section
    template_name = 'sections.html'
    context_object_name = 'sections'



class Categories(ListView):
    model = Category
    template_name = 'categories.html'
    context_object_name = 'categories'

    def render_to_response(self, context, **response_kwargs):
        if context['error'] == 'error':
            return render(self.request, 'pageNotFound404.html',  context, **response_kwargs, status=404)
        return super().render_to_response(context, **response_kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sections = Section.objects.all()
        try:
            section = Section.objects.get(slug=self.kwargs['slug'])
            categories = Category.objects.filter(section=section.id)
            context['sections'] = sections
            context['section'] = section
            context['categories'] = categories
            context['error'] = ''
        except:

            context['error'] = 'error'
        return context














# class Catalog(ListView):
#     model = Book
#     template_name = 'catalog.html'
#     context_object_name = 'books'
#     paginate_by = 5
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['section'] = Section.objects.all()
#         return context
#
#
#
#
#
# class AboutBook(DetailView):
#     model = Book
#     template_name = 'book.html'
#     context_object_name = 'book'
#     pk_url_kwarg = 'book_id'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         book = Book.objects.get(id=self.kwargs['product_id'])
#         feedbacks = book.feedback_set.all()
#         context['feedbacks'] = feedbacks
#         return context
#

