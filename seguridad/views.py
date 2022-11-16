from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, TemplateView

from proyecto.models import Proyecto
from seguridad.models import Usuario, Mensaje


# Create your views here.
def login(request):
    return render(request, 'seguridad/login.html')

def mensaje_crear(request):
    mensaje = Mensaje()
    mensaje.nombre = request.POST.get('nombre')
    mensaje.asunto = request.POST.get('asunto')
    mensaje.mensaje = request.POST.get('mensaje')
    mensaje.correo = request.POST.get('correo')
    mensaje.usuario = request.user
    mensaje.save()
    return redirect('/curriculum2')

@login_required
def home(request):
    return redirect('/admin')

class Curriculum(LoginRequiredMixin, TemplateView):
    model = Usuario
    template_name = 'curriculum/curriculum.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario =  self.request.user
        proyectos = Proyecto.objects.filter(usuario=usuario).all()
        context['usuario'] = usuario
        context['proyectos'] = proyectos
        return context

class CurriculumIndex(LoginRequiredMixin, TemplateView):
    model = Usuario
    template_name = 'curriculum/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario =  self.request.user
        proyectos = Proyecto.objects.filter(usuario=usuario).all()
        context['usuario'] = usuario
        context['proyectos'] = proyectos
        return context