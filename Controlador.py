from flask import Flask, abort
from flask_restful import Api, Resource, reqparse
from flasgger import Swagger, swag_from
from flask_restful_swagger_2 import Api as SwaggerApi
from Servicios import MatriculaService, UsuarioService, EstudianteService, DocenteService, PlanDeEstudioService, OfertaDeGruposService, CalificacionesService, CertificadoService, IngresosEgresosService, CuentasContablesService
from Repositorio import CalificacionRepository, CertificadoRepository, CuentaContableRepository, DocenteRepository, EstudianteRepository, IngresosEgresosRepository, MatriculaRepository, OfertaDeGruposRepository, PlanDeEstudioRepository, UsuarioRepository

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)
usuario_service = UsuarioService(UsuarioRepository())  
estudiante_service = EstudianteService(EstudianteRepository())  
docente_service = DocenteService(DocenteRepository())  
plan_de_estudio_service = PlanDeEstudioService(PlanDeEstudioRepository())  
oferta_de_grupos_service = OfertaDeGruposService(OfertaDeGruposRepository())  
calificaciones_service = CalificacionesService(CalificacionRepository())  
matricula_service = MatriculaService(MatriculaRepository())  
certificado_service = CertificadoService(CertificadoRepository())  
ingresos_egresos_service = IngresosEgresosService(IngresosEgresosRepository())  
cuentas_contables_service = CuentasContablesService(CuentaContableRepository())  


# Recurso para gestionar información de usuarios
#Controlador para Usuarios
class UsuarioResource(Resource):
    @swag_from('swagger/usuario_get.yml')  # Ruta a la descripción Swagger YAML
    def get(self, usuario_id):
        """
        Obtiene información de un usuario por ID.

        :param int usuario_id: ID del usuario.
        :return: Información del usuario.
        """
        usuario = usuario_service.obtener_usuario_por_id(usuario_id)
        if usuario:
            return {'id': usuario.id, 'nombre': usuario.nombre}
        else:
            abort(404, error='Usuario no encontrado')

# Agrega el recurso al API
api.add_resource(UsuarioResource, '/usuarios/<int:usuario_id>')

# Controlador para Estudiantes
class EstudianteResource(Resource):
    @swag_from('swagger/estudiante_get.yml')
    def get(self, estudiante_id):
        """
        Obtiene información de un estudiante por ID.

        :param int estudiante_id: ID del estudiante.
        :return: Información del estudiante.
        """
        estudiante = estudiante_service.obtener_estudiante_por_id(estudiante_id)
        if estudiante:
            return {'id': estudiante.id, 'nombre': estudiante.nombre}
        else:
            abort(404, error='Estudiante no encontrado')

api.add_resource(EstudianteResource, '/estudiantes/<int:estudiante_id>')

# Controlador para Docentes
class DocenteResource(Resource):
    @swag_from('swagger/docente_get.yml')
    def get(self, docente_id):
        """
        Obtiene información de un docente por ID.

        :param int docente_id: ID del docente.
        :return: Información del docente.
        """
        docente = docente_service.obtener_docente_por_id(docente_id)
        if docente:
            return {'id': docente.id, 'nombre': docente.nombre, 'materia': docente.materia}
        else:
            abort(404, error='Docente no encontrado')

    @swag_from('swagger/docente_post.yml')
    def post(self):
        """
        Agrega un nuevo docente.

        :return: Información del docente agregado.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', type=str, required=True, help='Nombre del docente')
        parser.add_argument('materia', type=str, required=True, help='Materia que enseña')
        args = parser.parse_args()

        nuevo_docente = docente_service.agregar_docente(args['nombre'], args['materia'])
        return {'id': nuevo_docente.id, 'nombre': nuevo_docente.nombre, 'materia': nuevo_docente.materia}, 201

api.add_resource(DocenteResource, '/docentes/<int:docente_id>', '/docentes')

# Controlador para Plan de Estudio
class PlanDeEstudioResource(Resource):
    def get(self, plan_id):
        """
        Obtiene información de un plan de estudio por ID.
        ---
        tags:
          - Plan de Estudio
        parameters:
          - name: plan_id
            in: path
            required: true
            type: integer
            description: ID del plan de estudio
        responses:
          '200':
            description: Información del plan de estudio
            schema:
              type: object
              properties:
                id:
                  type: integer
                  description: ID del plan de estudio
                nombre:
                  type: string
                  description: Nombre del plan de estudio
                niveles:
                  type: integer
                  description: Número de niveles del plan de estudio
          '404':
            description: Plan de estudio no encontrado
        """
        plan = plan_de_estudio_service.obtener_plan_por_id(plan_id)
        if plan:
            return {'id': plan.id, 'nombre': plan.nombre, 'niveles': plan.niveles}
        else:
            abort(404, error='Plan de estudio no encontrado')

    def post(self):
        """
        Agrega un nuevo plan de estudio.
        ---
        tags:
          - Plan de Estudio
        parameters:
          - name: nombre
            in: formData
            type: string
            required: true
            description: Nombre del plan de estudio
          - name: niveles
            in: formData
            type: integer
            required: true
            description: Número de niveles del plan de estudio
        responses:
          '201':
            description: Plan de estudio creado exitosamente
            schema:
              type: object
              properties:
                id:
                  type: integer
                  description: ID del nuevo plan de estudio
                nombre:
                  type: string
                  description: Nombre del nuevo plan de estudio
                niveles:
                  type: integer
                  description: Número de niveles del nuevo plan de estudio
        """
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', type=str, required=True, help='Nombre del plan de estudio')
        parser.add_argument('niveles', type=int, required=True, help='Número de niveles del plan de estudio')
        args = parser.parse_args()

        nuevo_plan = plan_de_estudio_service.agregar_plan(args['nombre'], args['niveles'])
        nuevo_plan = plan_de_estudio_service.agregar_plan(args['nombre'], args['niveles'])
        return {'id': nuevo_plan.id, 'nombre': nuevo_plan.nombre, 'niveles': nuevo_plan.niveles}, 201

# Agrega el recurso al API
api.add_resource(PlanDeEstudioResource, '/planes-de-estudio/<int:plan_id>', '/planes-de-estudio')


# Controlador para Oferta de Grupos
class OfertaDeGruposResource(Resource):
    def get(self, grupo_id):
        """
        Obtiene información de un grupo de la oferta por ID.
        ---
        tags:
          - Oferta de Grupos
        parameters:
          - name: grupo_id
            in: path
            required: true
            type: integer
            description: ID del grupo en la oferta
        responses:
          '200':
            description: Información del grupo en la oferta
            schema:
              type: object
              properties:
                id:
                  type: integer
                  description: ID del grupo en la oferta
                nombre:
                  type: string
                  description: Nombre del grupo
                materia:
                  type: string
                  description: Materia del grupo
                docente_id:
                  type: integer
                  description: ID del docente asignado al grupo
                espacio_fisico:
                  type: string
                  description: Espacio físico asignado al grupo
                horario:
                  type: string
                  description: Horario del grupo
          '404':
            description: Grupo en la oferta no encontrado
        """
        grupo = oferta_de_grupos_service.obtener_grupo_por_id(grupo_id)
        if grupo:
            return {'id': grupo.id, 'nombre': grupo.nombre, 'materia': grupo.materia,
                    'docente_id': grupo.docente_id, 'espacio_fisico': grupo.espacio_fisico,
                    'horario': grupo.horario}
        else:
            abort(404, error='Grupo en la oferta no encontrado')

    def post(self):
        """
        Agrega un nuevo grupo a la oferta.
        ---
        tags:
          - Oferta de Grupos
        parameters:
          - name: nombre
            in: formData
            type: string
            required: true
            description: Nombre del grupo
          - name: materia
            in: formData
            type: string
            required: true
            description: Materia del grupo
          - name: docente_id
            in: formData
            type: integer
            required: true
            description: ID del docente asignado al grupo
          - name: espacio_fisico
            in: formData
            type: string
            required: true
            description: Espacio físico asignado al grupo
          - name: horario
            in: formData
            type: string
            required: true
            description: Horario del grupo
        responses:
          '201':
            description: Grupo en la oferta creado exitosamente
            schema:
              type: object
              properties:
                id:
                  type: integer
                  description: ID del nuevo grupo en la oferta
                nombre:
                  type: string
                  description: Nombre del nuevo grupo
                materia:
                  type: string
                  description: Materia del nuevo grupo
                docente_id:
                  type: integer
                  description: ID del nuevo docente asignado al grupo
                espacio_fisico:
                  type: string
                  description: Espacio físico asignado al nuevo grupo
                horario:
                  type: string
                  description: Horario del nuevo grupo
        """
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', type=str, required=True, help='Nombre del grupo')
        parser.add_argument('materia', type=str, required=True, help='Materia del grupo')
        parser.add_argument('docente_id', type=int, required=True, help='ID del docente asignado')
        parser.add_argument('espacio_fisico', type=str, required=True, help='Espacio físico asignado')
        parser.add_argument('horario', type=str, required=True, help='Horario del grupo')
        args = parser.parse_args()

        nuevo_grupo = oferta_de_grupos_service.agregar_grupo(args['nombre'], args['materia'],
                                                             args['docente_id'], args['espacio_fisico'],
                                                             args['horario'])
        return {'id': nuevo_grupo.id, 'nombre': nuevo_grupo.nombre, 'materia': nuevo_grupo.materia,
                'docente_id': nuevo_grupo.docente_id, 'espacio_fisico': nuevo_grupo.espacio_fisico,
                'horario': nuevo_grupo.horario}, 201

# Agrega el recurso al API
api.add_resource(OfertaDeGruposResource, '/oferta-de-grupos/<int:grupo_id>', '/oferta-de-grupos')

# Controlador para Calificaciones
class CalificacionesResource(Resource):
    def get(self, estudiante_id, asignatura_id):
        """
        Obtiene la calificación de un estudiante en una asignatura.
        ---
        tags:
          - Calificaciones
        parameters:
          - name: estudiante_id
            in: path
            required: true
            type: integer
            description: ID del estudiante
          - name: asignatura_id
            in: path
            required: true
            type: integer
            description: ID de la asignatura
        responses:
          '200':
            description: Calificación del estudiante en la asignatura
            schema:
              type: object
              properties:
                estudiante_id:
                  type: integer
                  description: ID del estudiante
                asignatura_id:
                  type: integer
                  description: ID de la asignatura
                calificacion:
                  type: float
                  description: Calificación del estudiante en la asignatura
          '404':
            description: Calificación no encontrada
        """
        calificacion = calificaciones_service.obtener_calificacion(estudiante_id, asignatura_id)
        if calificacion:
            return {'estudiante_id': calificacion.estudiante_id,
                    'asignatura_id': calificacion.asignatura_id,
                    'calificacion': calificacion.calificacion}
        else:
            abort(404, error='Calificación no encontrada')

    def post(self):
        """
        Agrega una nueva calificación para un estudiante en una asignatura.
        ---
        tags:
          - Calificaciones
        parameters:
          - name: estudiante_id
            in: formData
            type: integer
            required: true
            description: ID del estudiante
          - name: asignatura_id
            in: formData
            type: integer
            required: true
            description: ID de la asignatura
          - name: calificacion
            in: formData
            type: float
            required: true
            description: Calificación del estudiante en la asignatura
        responses:
          '201':
            description: Calificación creada exitosamente
            schema:
              type: object
              properties:
                estudiante_id:
                  type: integer
                  description: ID del estudiante
                asignatura_id:
                  type: integer
                  description: ID de la asignatura
                calificacion:
                  type: float
                  description: Calificación del estudiante en la asignatura
        """
        parser = reqparse.RequestParser()
        parser.add_argument('estudiante_id', type=int, required=True, help='ID del estudiante')
        parser.add_argument('asignatura_id', type=int, required=True, help='ID de la asignatura')
        parser.add_argument('calificacion', type=float, required=True, help='Calificación del estudiante')
        args = parser.parse_args()

        nueva_calificacion = calificaciones_service.agregar_calificacion(args['estudiante_id'], args['asignatura_id'],
                                                                          args['calificacion'])
        return {'estudiante_id': nueva_calificacion.estudiante_id,
                'asignatura_id': nueva_calificacion.asignatura_id,
                'calificacion': nueva_calificacion.calificacion}, 201

# Agrega el recurso al API
api.add_resource(CalificacionesResource, '/calificaciones/<int:estudiante_id>/<int:asignatura_id>', '/calificaciones')

# Controlador para Matrículas
class MatriculaResource(Resource):
    def get(self, estudiante_id, grupo_id):
        """
        Obtiene la información de matrícula de un estudiante en un grupo.
        ---
        tags:
          - Matrículas
        parameters:
          - name: estudiante_id
            in: path
            required: true
            type: integer
            description: ID del estudiante
          - name: grupo_id
            in: path
            required: true
            type: integer
            description: ID del grupo
        responses:
          '200':
            description: Información de matrícula del estudiante en el grupo
            schema:
              type: object
              properties:
                estudiante_id:
                  type: integer
                  description: ID del estudiante
                grupo_id:
                  type: integer
                  description: ID del grupo
                fecha_matricula:
                  type: string
                  description: Fecha de matrícula
          '404':
            description: Matrícula no encontrada
        """
        matricula = matricula_service.obtener_matricula(estudiante_id, grupo_id)
        if matricula:
            return {'estudiante_id': matricula.estudiante_id, 'grupo_id': matricula.grupo_id,
                    'fecha_matricula': matricula.fecha_matricula}
        else:
            abort(404, error='Matrícula no encontrada')

    def post(self):
        """
        Agrega una nueva matrícula para un estudiante en un grupo.
        ---
        tags:
          - Matrículas
        parameters:
          - name: estudiante_id
            in: formData
            type: integer
            required: true
            description: ID del estudiante
          - name: grupo_id
            in: formData
            type: integer
            required: true
            description: ID del grupo
        responses:
          '201':
            description: Matrícula creada exitosamente
            schema:
              type: object
              properties:
                estudiante_id:
                  type: integer
                  description: ID del estudiante
                grupo_id:
                  type: integer
                  description: ID del grupo
                fecha_matricula:
                  type: string
                  description: Fecha de matrícula
        """
        parser = reqparse.RequestParser()
        parser.add_argument('estudiante_id', type=int, required=True, help='ID del estudiante')
        parser.add_argument('grupo_id', type=int, required=True, help='ID del grupo')
        args = parser.parse_args()

        nueva_matricula = matricula_service.agregar_matricula(args['estudiante_id'], args['grupo_id'])
        return {'estudiante_id': nueva_matricula.estudiante_id, 'grupo_id': nueva_matricula.grupo_id,
                'fecha_matricula': nueva_matricula.fecha_matricula}, 201

# Agrega el recurso al API
api.add_resource(MatriculaResource, '/matriculas/<int:estudiante_id>/<int:grupo_id>', '/matriculas')

# Controlador para Certificados
class CertificadoResource(Resource):
    def get(self, estudiante_id):
        """
        Obtiene la información del certificado de un estudiante.
        ---
        tags:
          - Certificados
        parameters:
          - name: estudiante_id
            in: path
            required: true
            type: integer
            description: ID del estudiante
        responses:
          '200':
            description: Información del certificado del estudiante
            schema:
              type: object
              properties:
                estudiante_id:
                  type: integer
                  description: ID del estudiante
                fecha_emision:
                  type: string
                  description: Fecha de emisión del certificado
          '404':
            description: Certificado no encontrado
        """
        certificado = certificado_service.obtener_certificado(estudiante_id)
        if certificado:
            return {'estudiante_id': certificado.estudiante_id, 'fecha_emision': certificado.fecha_emision}
        else:
            abort(404, error='Certificado no encontrado')

    def post(self):
        """
        Emite un nuevo certificado para un estudiante.
        ---
        tags:
          - Certificados
        parameters:
          - name: estudiante_id
            in: formData
            type: integer
            required: true
            description: ID del estudiante
        responses:
          '201':
            description: Certificado emitido exitosamente
            schema:
              type: object
              properties:
                estudiante_id:
                  type: integer
                  description: ID del estudiante
                fecha_emision:
                  type: string
                  description: Fecha de emisión del certificado
        """
        parser = reqparse.RequestParser()
        parser.add_argument('estudiante_id', type=int, required=True, help='ID del estudiante')
        args = parser.parse_args()

        nuevo_certificado = certificado_service.emitir_certificado(args['estudiante_id'])
        return {'estudiante_id': nuevo_certificado.estudiante_id, 'fecha_emision': nuevo_certificado.fecha_emision}, 201

# Agrega el recurso al API
api.add_resource(CertificadoResource, '/certificados/<int:estudiante_id>', '/certificados')


# Controlador para Ingresos y Egresos
class IngresosEgresosResource(Resource):
    def post(self):
        """
        Agrega una nueva transacción de Ingresos o Egresos.
        ---
        tags:
          - Ingresos y Egresos
        parameters:
          - name: tipo
            in: formData
            type: string
            required: true
            description: Tipo de transacción (Ingreso/Egreso)
          - name: monto
            in: formData
            type: number
            required: true
            description: Monto de la transacción
          - name: descripcion
            in: formData
            type: string
            required: true
            description: Descripción de la transacción
          - name: cuenta_contable_id
            in: formData
            type: integer
            required: true
            description: ID de la cuenta contable asociada
        responses:
          '201':
            description: Transacción agregada exitosamente
            schema:
              type: object
              properties:
                id:
                  type: integer
                  description: ID de la transacción
                tipo:
                  type: string
                  description: Tipo de transacción (Ingreso/Egreso)
                monto:
                  type: number
                  description: Monto de la transacción
                descripcion:
                  type: string
                  description: Descripción de la transacción
                cuenta_contable_id:
                  type: integer
                  description: ID de la cuenta contable asociada
        """
        parser = reqparse.RequestParser()
        parser.add_argument('tipo', type=str, required=True, help='Tipo de transacción (Ingreso/Egreso)')
        parser.add_argument('monto', type=float, required=True, help='Monto de la transacción')
        parser.add_argument('descripcion', type=str, required=True, help='Descripción de la transacción')
        parser.add_argument('cuenta_contable_id', type=int, required=True, help='ID de la cuenta contable asociada')
        args = parser.parse_args()

        nueva_transaccion = ingresos_egresos_service.agregar_transaccion(args['tipo'], args['monto'],
                                                                         args['descripcion'], args['cuenta_contable_id'])
        return {'id': nueva_transaccion.id, 'tipo': nueva_transaccion.tipo, 'monto': nueva_transaccion.monto,
                'descripcion': nueva_transaccion.descripcion, 'cuenta_contable_id': nueva_transaccion.cuenta_contable_id}, 201

# Agrega el recurso al API
api.add_resource(IngresosEgresosResource, '/transacciones')

# Controlador para Cuentas Contables
class CuentasContablesResource(Resource):
    def get(self):
        """
        Obtiene la lista de cuentas contables.
        ---
        tags:
          - Cuentas Contables
        responses:
          '200':
            description: Lista de cuentas contables
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                    description: ID de la cuenta contable
                  nombre:
                    type: string
                    description: Nombre de la cuenta contable
        """
        cuentas_contables = cuentas_contables_service.obtener_cuentas_contables()
        return [{'id': cuenta.id, 'nombre': cuenta.nombre} for cuenta in cuentas_contables]

    def post(self):
        """
        Agrega una nueva cuenta contable.
        ---
        tags:
          - Cuentas Contables
        parameters:
          - name: nombre
            in: formData
            type: string
            required: true
            description: Nombre de la cuenta contable
        responses:
          '201':
            description: Cuenta contable agregada exitosamente
            schema:
              type: object
              properties:
                id:
                  type: integer
                  description: ID de la cuenta contable
                nombre:
                  type: string
                  description: Nombre de la cuenta contable
        """
        parser = reqparse.RequestParser()
        parser.add_argument('nombre', type=str, required=True, help='Nombre de la cuenta contable')
        args = parser.parse_args()

        nueva_cuenta_contable = cuentas_contables_service.agregar_cuenta_contable(args['nombre'])
        return {'id': nueva_cuenta_contable.id, 'nombre': nueva_cuenta_contable.nombre}, 201

# Agrega el recurso al API
api.add_resource(CuentasContablesResource, '/cuentas-contables')

if __name__ == '__main__':
    app.run(debug=True)