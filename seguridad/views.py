from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, TemplateView

from proyecto.models import Proyecto
from seguridad.models import Usuario


# Create your views here.
def login(request):
    return render(request, 'seguridad/login.html')

@login_required
def home(request):
    return redirect('/admin')

# @login_required
# def curriculum(request):
#     usuario = request.user
#     proyectos = Proyecto.objects.filter(usuario=usuario).all()
#     print(proyectos)
#     return render(request, 'curriculum/curriculum.html', locals())

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
