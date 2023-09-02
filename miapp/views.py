from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Dork
from django.db.models import Q
from .models import Onion


def mi_vista(request):
    search_query = request.GET.get("q", "")
    dorks_list = Dork.objects.all()

    if search_query:
        dorks_list = dorks_list.filter(
            Q(titulo__icontains=search_query) | Q(dork__icontains=search_query)
        )

    paginator = Paginator(dorks_list, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, "mi_vista.html", {"page_obj": page_obj, "search_query": search_query}
    )


def acerca_de(request):
    search_query = request.GET.get("q", "")
    onions_list = Onion.objects.all()  # Utiliza el modelo Onion

    if search_query:
        onions_list = onions_list.filter(
            Q(pagina__icontains=search_query) | Q(onion__icontains=search_query)
        )

    paginator = Paginator(onions_list, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, "acerca_de.html", {"page_obj": page_obj, "search_query": search_query}
    )


def soporte(request):
    return render(request, "soporte.html")


def preguntas_frecuentes(request):
    return render(request, "preguntas_frecuentes.html")


def herramientas(request):
    return render(request, "herramientas.html")
