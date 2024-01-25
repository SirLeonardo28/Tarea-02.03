# test_servicios.py
from unittest.mock import Mock
import pytest
from Modelo import Calificacion, CuentaContable, Matricula, OfertaDeGrupos, Transaccion
from Servicios import ( UsuarioService,EstudianteService,DocenteService,PlanDeEstudioService,OfertaDeGruposService,CalificacionesService,MatriculaService,
    CertificadoService,
    IngresosEgresosService,
    CuentasContablesService,
)

# Pruebas para UsuarioService
def test_obtener_usuario_por_id():
    usuario_repository_mock = Mock()
    usuario_service = UsuarioService(usuario_repository_mock)

    result = usuario_service.obtener_usuario_por_id(1)

    usuario_repository_mock.obtener_por_id.assert_called_once_with(1)
    assert result == usuario_repository_mock.obtener_por_id.return_value

# Pruebas para EstudianteService
def test_obtener_estudiante_por_id():
    estudiante_repository_mock = Mock()
    estudiante_service = EstudianteService(estudiante_repository_mock)

    result = estudiante_service.obtener_estudiante_por_id(1)

    estudiante_repository_mock.obtener_por_id.assert_called_once_with(1)
    assert result == estudiante_repository_mock.obtener_por_id.return_value

# Pruebas para DocenteService
def test_obtener_docente_por_id():
    docente_repository_mock = Mock()
    docente_service = DocenteService(docente_repository_mock)

    result = docente_service.obtener_docente_por_id(1)

    docente_repository_mock.obtener_por_id.assert_called_once_with(1)
    assert result == docente_repository_mock.obtener_por_id.return_value

# Pruebas para PlanDeEstudioService
def test_obtener_plan_de_estudio_por_id():
    plan_repository_mock = Mock()
    plan_service = PlanDeEstudioService(plan_repository_mock)

    result = plan_service.obtener_plan_de_estudio_por_id(1)

    plan_repository_mock.obtener_por_id.assert_called_once_with(1)
    assert result == plan_repository_mock.obtener_por_id.return_value


# Ejemplo de prueba para OfertaDeGruposService
def test_obtener_grupo():
    grupo_repository_mock = Mock()
    grupo_service = OfertaDeGruposService(grupo_repository_mock)

    # Configurar el comportamiento del Mock para simular una llamada al método obtener_por_id
    grupo_repository_mock.obtener_por_id.return_value = OfertaDeGrupos(
        id=1, nombre="Grupo1", materia="Materia1", docente_id=1, espacio_fisico="Aula1", horario="Lunes 8:00-10:00"
    )

    # Ejecución de prueba
    result = grupo_service.obtener_grupo(1)

    # Verificación de resultados
    grupo_repository_mock.obtener_por_id.assert_called_once_with(1)
    assert result.id == 1
    assert result.nombre == "Grupo1"
    assert result.materia == "Materia1"  
def test_obtener_calificacion():
    calificacion_repository_mock = Mock()
    calificacion_service = CalificacionesService(calificacion_repository_mock)

    # Ejecución de prueba
    result = calificacion_service.obtener_calificacion(1, 2)

    # Verificación de resultados
    calificacion_repository_mock.obtener_por_estudiante_y_asignatura.assert_called_once_with(1, 2)
    assert result == calificacion_repository_mock.obtener_por_estudiante_y_asignatura.return_value  
def test_obtener_matricula():
    matricula_repository_mock = Mock()
    matricula_service = MatriculaService(matricula_repository_mock)

    # Ejecución de prueba
    result = matricula_service.obtener_matricula(1)

    # Verificación de resultados
    matricula_repository_mock.obtener_por_estudiante.assert_called_once_with(1)
    assert result == matricula_repository_mock.obtener_por_estudiante.return_value  

def test_obtener_certificado():
    certificado_repository_mock = Mock()
    certificado_service = CertificadoService(certificado_repository_mock)

    # Ejecución de prueba
    result = certificado_service.obtener_certificado(1, "2023-01")

    # Verificación de resultados
    certificado_repository_mock.obtener_por_estudiante_y_periodo.assert_called_once_with(1, "2023-01")
    assert result == certificado_repository_mock.obtener_por_estudiante_y_periodo.return_value  

def test_agregar_transaccion():
    ingresos_egresos_repository_mock = Mock()
    ingresos_egresos_service = IngresosEgresosService(ingresos_egresos_repository_mock)

    # Ejecución de prueba
    result = ingresos_egresos_service.agregar_transaccion("Ingreso", 100, "Pago de matrícula", 1)

    # Verificación de resultados
    ingresos_egresos_repository_mock.agregar_transaccion.assert_called_once_with(
        Transaccion(tipo="Ingreso", monto=100, descripcion="Pago de matrícula", cuenta_contable_id=1)
    )
    assert result == ingresos_egresos_repository_mock.agregar_transaccion.return_value  

# Ejemplo de prueba para CuentasContablesService
def test_obtener_cuentas_contables():
    cuentas_contables_repository_mock = Mock()
    cuentas_contables_service = CuentasContablesService(cuentas_contables_repository_mock)

    # Ejecución de prueba
    result = cuentas_contables_service.obtener_cuentas_contables()

    # Verificación de resultados
    cuentas_contables_repository_mock.obtener_cuentas_contables.assert_called_once()
    assert result == cuentas_contables_repository_mock.obtener_cuentas_contables.return_value

# Con esto se ejecutan todas las pruebas
if __name__ == '__main__':
    pytest.main(['-v', 'test_servicios.py'])