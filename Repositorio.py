# repositorios.py
from Modelo import Usuario, Estudiante, Docente, PlanDeEstudio, OfertaDeGrupos, Calificacion, Matricula, Certificado, Transaccion, CuentaContable

class UsuarioRepository:
    def obtener_por_id(self, usuario_id):
        # Lógica para obtener un usuario por ID desde la base de datos
        pass

class EstudianteRepository:
    def obtener_por_id(self, estudiante_id):
        # Lógica para obtener un estudiante por ID desde la base de datos
        pass

class DocenteRepository:
    def obtener_por_id(self, docente_id):
        # Lógica para obtener un docente por ID desde la base de datos
        pass

class PlanDeEstudioRepository:
    def obtener_por_id(self, plan_id):
        # Lógica para obtener un plan de estudio por ID desde la base de datos
        pass

class OfertaDeGruposRepository:
    def obtener_por_id(self, grupo_id):
        # Lógica para obtener un grupo por ID desde la base de datos
        pass

class CalificacionRepository:
    def obtener_por_estudiante_y_asignatura(self, estudiante_id, asignatura_id):
        # Lógica para obtener una calificación por estudiante y asignatura desde la base de datos
        pass

class MatriculaRepository:
    def obtener_por_estudiante(self, estudiante_id):
        # Lógica para obtener una matrícula por estudiante desde la base de datos
        pass

class CertificadoRepository:
    def obtener_por_estudiante_y_periodo(self, estudiante_id, periodo_lectivo):
        # Lógica para obtener un certificado por estudiante y período desde la base de datos
        pass

class IngresosEgresosRepository:
    def __init__(self):
        self.transacciones = []

    def agregar_transaccion(self, transaccion: Transaccion):
        self.transacciones.append(transaccion)
        return transaccion

class CuentaContableRepository:
    def __init__(self):
        self.cuentas_contables = []

    def obtener_cuentas_contables(self):
        return self.cuentas_contables

    def agregar_cuenta_contable(self, cuenta_contable: CuentaContable):
        self.cuentas_contables.append(cuenta_contable)
        return cuenta_contable