
class ProyectoAppService(object):

    @staticmethod
    def puede_guardar_proyecto(proyecto, usuario):
        return proyecto.usuario == usuario

    @staticmethod
    def puede_guardar_mensaje(mensaje, usuario):
        return True if mensaje and usuario else False

    @staticmethod
    def puede_guardar_habilidad(habilidad, usuario):
        return habilidad.usuario == usuario