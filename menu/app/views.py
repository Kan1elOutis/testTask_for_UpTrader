from django.db import connection
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView

from app.models import Menu


class MenuView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.filter(slug='main_menu').first()
        return context

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        response = super().get(request, *args, **kwargs)

        # Сколько запросов к бд
        print("Number of database queries: ", len(connection.queries))

        return response
