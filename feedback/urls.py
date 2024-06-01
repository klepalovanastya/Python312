from django.urls import path, re_path

import feedback.views as feedback

urlpatterns = [

    path('', feedback.page_feedback),


]