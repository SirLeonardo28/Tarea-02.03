# modelos.py

class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

class Estudiante:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

class Docente:
    def __init__(self, id, nombre, materia):
        self.id = id
        self.nombre = nombre
        self.materia = materia

class PlanDeEstudio:
    def __init__(self, id, nombre, niveles):
        self.id = id
        self.nombre = nombre
        self.niveles = niveles

class OfertaDeGrupos:
    def __init__(self, id, nombre, materia, docente_id, espacio_fisico, horario):
        self.id = id
        self.nombre = nombre
        self.materia = materia
        self.docente_id = docente_id
        self.espacio_fisico = espacio_fisico
        self.horario = horario

class Calificacion:
    def __init__(self, estudiante_id, asignatura_id, calificacion):
        self.estudiante_id = estudiante_id
        self.asignatura_id = asignatura_id
        self.calificacion = calificacion

class Matricula:
    def __init__(self, estudiante_id, rubros_cobro):
        self.estudiante_id = estudiante_id
        self.rubros_cobro = rubros_cobro

class Certificado:
    def __init__(self, estudiante_id, nombre_estudiante, periodo_lectivo, calificaciones):
        self.estudiante_id = estudiante_id
        self.nombre_estudiante = nombre_estudiante
        self.periodo_lectivo = periodo_lectivo
        self.calificaciones = calificaciones

class Transaccion:
    def __init__(self, tipo, monto, descripcion, cuenta_contable_id):
        self.tipo = tipo
        self.monto = monto
        self.descripcion = descripcion
        self.cuenta_contable_id = cuenta_contable_id

class CuentaContable:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre