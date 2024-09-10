from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from dogs.models import Dog



class ShowDogsView(TemplateView):
    template_name = "dogs/show_students.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['dogs'] = Dog.objects.all()
        return context

# class ShowDogsView(View):
#     def get(request, *args **kwargs):
#         dogs = Dog.objects.all()

#         result = ""
#         for s in dogs:
#             result += s.name + "<br>"
#         return HttpResponse(result)

# # Create your views here.
# def show_dogs(request):
#     return HttpResponse("Привет")