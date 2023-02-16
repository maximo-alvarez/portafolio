import datetime

from django.test import SimpleTestCase

from app.proyecto.layer.proyecto import ProyectoAppService
from app.proyecto.models import Habilidad, Proyecto, Categoria
from app.seguridad.models import Mensaje, Usuario

class TestPortafolioAppService(SimpleTestCase):

    def setUp(self):
        self.usuario_actual = Usuario(id=1)
        self.usuario_auxiliar = Usuario(id=2)
        self.categoria = Categoria(id=1)
        self.proyecto = Proyecto(
            id=1,
            nombre='Proyecto 1',
            fecha=datetime.datetime.now(),
            descripcion='Descripción del proyecto',
            url_git='https://gitlab.com/maalvarezp',
            url_proyecto='https://perfilprofesional.com',
            usuario=self.usuario_auxiliar,
            categoria=self.categoria
        )
        self.habilidad = Habilidad(
            id=1,
            nombre='Habilidad 1',
            porcentaje=90,
            usuario=self.usuario_auxiliar
        )
        self.mensaje = Mensaje(
            id=1,
            asunto='Asunto',
            correo='maxandres90@gmail.com',
            mensaje='Mensaje',
            nombre='Máximo Álvarez',
            usuario=self.usuario_auxiliar
        )

    def test_puede_crear_proyecto(self):
        self.assertTrue(ProyectoAppService.puede_guardar_proyecto(self.proyecto, self.usuario_auxiliar))

    def test_puede_crear_mensaje(self):
        self.assertTrue(ProyectoAppService.puede_guardar_mensaje(self.mensaje, self.usuario_auxiliar))

    def test_puede_crear_habilidad(self):
        self.assertTrue(ProyectoAppService.puede_guardar_habilidad(self.habilidad, self.usuario_auxiliar))


    def test_no_puede_crear_proyecto(self):
        self.assertFalse(ProyectoAppService.puede_guardar_proyecto(self.proyecto, self.usuario_actual))

    def test_no_puede_crear_mensaje(self):
        self.assertFalse(ProyectoAppService.puede_guardar_mensaje(self.mensaje, None))

    def test_no_puede_guardar_habilidad(self):
        self.assertFalse(ProyectoAppService.puede_guardar_habilidad(self.habilidad, self.usuario_actual))

