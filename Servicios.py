# servicios.py
from Repositorio import CalificacionRepository, CertificadoRepository, CuentaContableRepository, IngresosEgresosRepository, MatriculaRepository, OfertaDeGruposRepository, PlanDeEstudioRepository, UsuarioRepository, EstudianteRepository, DocenteRepository
from Modelo import Usuario, Estudiante, Docente, PlanDeEstudio, OfertaDeGrupos, Calificacion, Matricula, Certificado, Transaccion, CuentaContable
class UsuarioService:
    def __init__(self, usuario_repository: UsuarioRepository):
        self.usuario_repository = usuario_repository

    def obtener_usuario_por_id(self, usuario_id):
        return self.usuario_repository.obtener_por_id(usuario_id)

class EstudianteService:
    def __init__(self, estudiante_repository: EstudianteRepository):
        self.estudiante_repository = estudiante_repository

    def obtener_estudiante_por_id(self, estudiante_id):
        return self.estudiante_repository.obtener_por_id(estudiante_id)

class DocenteService:
    def __init__(self, docente_repository: DocenteRepository):
        self.docente_repository = docente_repository

    def obtener_docente_por_id(self, docente_id):
        return self.docente_repository.obtener_por_id(docente_id)

    def agregar_docente(self, nombre, materia):
        # Lógica para agregar un nuevo docente
        pass

class PlanDeEstudioService:
    def __init__(self, plan_de_estudio_repository: PlanDeEstudioRepository):
        self.plan_de_estudio_repository = plan_de_estudio_repository

    def obtener_plan_de_estudio_por_id(self, plan_id):
        return self.plan_de_estudio_repository.obtener_por_id(plan_id)

    def agregar_plan_de_estudio(self, nombre, niveles):
        # Lógica para agregar un nuevo plan de estudio
        nuevo_plan = PlanDeEstudio(id=None, nombre=nombre, niveles=niveles)  
        return self.plan_de_estudio_repository.agregar_plan_de_estudio(nuevo_plan)

class OfertaDeGruposService:
    def __init__(self, oferta_de_grupos_repository: OfertaDeGruposRepository):
        self.oferta_de_grupos_repository = oferta_de_grupos_repository

    def obtener_grupo(self, grupo_id):
        return self.oferta_de_grupos_repository.obtener_grupo(grupo_id)

    def agregar_grupo(self, nombre, materia, docente_id, espacio_fisico, horario):
        nuevo_grupo = OfertaDeGrupos(nombre, materia, docente_id, espacio_fisico, horario)
        return self.oferta_de_grupos_repository.agregar_grupo(nuevo_grupo)
    

class CalificacionesService:
    def __init__(self, calificaciones_repository: CalificacionRepository):
        self.calificaciones_repository = calificaciones_repository

    def obtener_calificacion(self, estudiante_id, asignatura_id):
        return self.calificaciones_repository.obtener_calificacion(estudiante_id, asignatura_id)

    def agregar_calificacion(self, estudiante_id, asignatura_id, calificacion):
        nueva_calificacion = Calificacion(estudiante_id, asignatura_id, calificacion)
        return self.calificaciones_repository.agregar_calificacion(nueva_calificacion)


class MatriculaService:
    def __init__(self, matriculas_repository: MatriculaRepository):
        self.matriculas_repository = matriculas_repository

    def obtener_matricula(self, estudiante_id):
        return self.matriculas_repository.obtener_matricula(estudiante_id)

    def agregar_matricula(self, estudiante_id, rubros_cobro):
        nueva_matricula = Matricula(estudiante_id, rubros_cobro)
        return self.matriculas_repository.agregar_matricula(nueva_matricula)

class CertificadoService:
    def __init__(self, certificados_repository: CertificadoRepository):
        self.certificados_repository = certificados_repository

    def obtener_certificado(self, estudiante_id, periodo_lectivo):
        return self.certificados_repository.obtener_certificado(estudiante_id, periodo_lectivo)

class IngresosEgresosService:
    def __init__(self, ingresos_egresos_repository: IngresosEgresosRepository):
        self.ingresos_egresos_repository = ingresos_egresos_repository

    def agregar_transaccion(self, tipo, monto, descripcion, cuenta_contable_id):
        nueva_transaccion = Transaccion(tipo, monto, descripcion, cuenta_contable_id)
        return self.ingresos_egresos_repository.agregar_transaccion(nueva_transaccion)

class CuentasContablesService:
    def __init__(self, cuentas_contables_repository: CuentaContableRepository):
        self.cuentas_contables_repository = cuentas_contables_repository

    def obtener_cuentas_contables(self):
        return self.cuentas_contables_repository.obtener_cuentas_contables()

    def agregar_cuenta_contable(self, nombre):
        nueva_cuenta_contable = CuentaContable(nombre)
        return self.cuentas_contables_repository.agregar_cuenta_contable(nueva_cuenta_contable)


