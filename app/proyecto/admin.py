from django.contrib import admin
from django import forms
from import_export.admin import ImportExportMixin

from app.proyecto.models import Categoria, Proyecto, Habilidad
from app.seguridad.models import Mensaje


class ProyectoAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion'].widget = forms.widgets.Textarea()

    class Meta:
        fields = ('nombre', 'descripcion', 'url_git', 'url_proyecto', 'categoria', 'foto')
        model = Proyecto


class ProyectoAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'usuario', 'foto')
    search_fields = ('usuario__email', 'cedula', )
    form = ProyectoAdminForm

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Proyecto.objects.all()
        return Proyecto.objects.filter(usuario=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        obj.save()


class MensajeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('correo', 'nombre', 'asunto', 'mensaje')
    def get_queryset(self, request):
        if request.user.is_superuser:
            return Mensaje.objects.all()
        return Mensaje.objects.filter(usuario=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        obj.save()


class HabilidadAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('nombre', 'porcentaje')
    def get_queryset(self, request):
        if request.user.is_superuser:
            return Habilidad.objects.all()
        return Habilidad.objects.filter(usuario=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.usuario = request.user
        obj.save()


admin.site.register(Categoria)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(Habilidad, HabilidadAdmin)