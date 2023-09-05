from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Dork
from django.db.models import Q
from .models import Onion
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DorkForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm


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


def listar_dorks(request):
    dorks = Dork.objects.all()
    return render(request, "crudork.html", {"dorks": dorks})


def crear_dork(request):
    if request.method == "POST":
        form = DorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_dorks")
    else:
        form = DorkForm()
    return render(request, "crear_dork.html", {"form": form})


def editar_dork(request, pk):
    dork = get_object_or_404(Dork, pk=pk)

    if request.method == "POST":
        form = DorkForm(request.POST, instance=dork)
        if form.is_valid():
            form.save()
            return redirect("listar_dorks")
    else:
        form = DorkForm(instance=dork)

    return render(request, "editar_dork.html", {"form": form})


def eliminar_dork(request, pk):
    dork = get_object_or_404(Dork, pk=pk)
    if request.method == "POST":
        dork.delete()
        return redirect("listar_dorks")


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Configura la contraseña manualmente
            user.save()
            login(request, user)  # Inicia sesión después del registro
            return redirect('mi_vista')  # Redirigir a la página deseada después del registro
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


def inicio_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('mi_vista')  # Redirige a la página deseada después del inicio de sesión
            else:
                # Manejar error de inicio de sesión (usuario o contraseña incorrectos)
                pass  # Puedes agregar tu propia lógica de manejo de errores aquí
    else:
        form = LoginForm()
    return render(request, 'inicio_sesion.html', {'form': form})



