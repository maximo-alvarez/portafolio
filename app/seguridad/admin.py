from django.contrib import admin

from django import forms
from import_export.admin import ImportExportMixin

from app.proyecto.models import Proyecto
from app.seguridad.models import Usuario, Mensaje


class MensajeInline(admin.TabularInline):
    model = Mensaje
    extra = 0

class ProyectoInline(admin.StackedInline):
    model = Proyecto
    extra = 0

class UsuarioAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descripcion'].widget = forms.widgets.Textarea()

    class Meta:
        fields = ('email', 'first_name', 'last_name', 'cedula', 'celular', 'descripcion', 'url_git', 'url_linkedin')
        model = Usuario


class UsuarioAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('username', 'cedula', 'email', 'first_name', 'last_name', 'is_active')
    search_fields = ('email', 'cedula', )
    form = UsuarioAdminForm

    inlines = [ProyectoInline]
    # inlines = [ProyectoInline, MensajeInline]

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Usuario.objects.all()
        return Usuario.objects.filter(id=request.user.id)


admin.site.register(Usuario, UsuarioAdmin)