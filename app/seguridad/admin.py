from django.contrib import admin

from django import forms
from import_export.admin import ImportExportMixin

from app.proyecto.models import Proyecto, Habilidad
from app.seguridad.models import Usuario, Mensaje


class MensajeInline(admin.TabularInline):
    model = Mensaje
    extra = 0

class ProyectoInline(admin.StackedInline):
    model = Proyecto
    extra = 0

class HabilidadInline(admin.TabularInline):
    model = Habilidad
    extra = 0

class UsuarioAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion'].widget = forms.widgets.Textarea()

    class Meta:
        fields = ('email', 'foto', 'first_name', 'last_name', 'cedula', 'celular', 'descripcion', 'url_git', 'url_linkedin', 'url_twitter', 'url_instagram')
        model = Usuario

class UsuarioAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('username', 'foto', 'cedula', 'email', 'first_name', 'last_name', 'is_active')
    search_fields = ('email', 'cedula', )
    form = UsuarioAdminForm

    inlines = [ProyectoInline, HabilidadInline]

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Usuario.objects.all()
        return Usuario.objects.filter(id=request.user.id)

admin.site.register(Usuario, UsuarioAdmin)