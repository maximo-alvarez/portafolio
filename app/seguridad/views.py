from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, TemplateView

from app.proyecto.models import Proyecto, Habilidad
from app.seguridad.models import Usuario, Mensaje


# Create your views here.
def login(request):
    return render(request, 'seguridad/login.html')

def mensaje_crear(request):
    mensaje = Mensaje()
    mensaje.nombre = request.POST.get('nombre')
    mensaje.asunto = request.POST.get('asunto')
    mensaje.mensaje = request.POST.get('mensaje')
    mensaje.correo = request.POST.get('correo')
    mensaje.usuario = Usuario.objects.filter(username=request.POST.get('username')).first()
    mensaje.save()
    return redirect('/curriculum')

@login_required
def home(request):
    return redirect('/admin')

class CurriculumIndex(TemplateView):
    model = Usuario
    template_name = 'curriculum/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario =  Usuario.objects.filter(username=kwargs['username']).first()
        proyectos = Proyecto.objects.filter(usuario=usuario).all()
        habilidades = Habilidad.objects.filter(usuario=usuario).all()
        context['usuario'] = usuario
        context['proyectos'] = proyectos
        context['habilidades'] = habilidades
        return context

class CurriculumIndexAdmin(LoginRequiredMixin, TemplateView):
    model = Usuario
    template_name = 'curriculum/index.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario =  self.request.user
        proyectos = Proyecto.objects.filter(usuario=usuario).all()
        habilidades = Habilidad.objects.filter(usuario=usuario).all()
        context['usuario'] = usuario
        context['proyectos'] = proyectos
        context['habilidades'] = habilidades
        return context
