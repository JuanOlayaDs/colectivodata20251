import pandas as pd

analisisUsuarios=pd.read_excel("./data/usuarios_sistema_completo.xlsx") 

#2. Solo profesores
soloProfesores=analisisUsuarios.query('tipo_usuario=="docente"')
print(soloProfesores)
#3. Todos excepto estudiantes
todosExceptoEstudiantes=analisisUsuarios.query('tipo_usuario!="estudiante"')
print(todosExceptoEstudiantes)
#4. Filtrar por especialidad
especialidad=analisisUsuarios.query('especialidad=="Ingenieria Ambiental"')
print(especialidad)
#5. Excluir una especialidad
excluirEspecialidad=analisisUsuarios.query('especialidad!="Ingenieraia de Sistemas"')
print(excluirEspecialidad)
#6. Excluir administrativos
excluirAdministrativos=analisisUsuarios.query('tipo_usuario!="administrativo,"')
print(excluirAdministrativos)
#7. Direcciones en medellin
medellin = analisisUsuarios[analisisUsuarios['direccion'].str.contains('medellin', case=False)]
print(medellin)


#8. Direcciones terminadas en sur
terminanSur = analisisUsuarios[analisisUsuarios['direccion'].str.endswith('sur')]
print(terminanSur)

#9. Direcciones que inician con calle
inicianCalle = analisisUsuarios[analisisUsuarios['direccion'].str.startswith('calle')]
print(inicianCalle)

#10.Especialidades que contienen la palabra datos
contienenDatos = analisisUsuarios[analisisUsuarios['especialidad'].str.contains('datos', case=False)]
print(contienenDatos)

#11. instructores en itagui

instructoresItagui = analisisUsuarios[(analisisUsuarios['tipo_usuario'] == 'instructor') & 
 (analisisUsuarios['direccion'].str.contains('itagui', case=False))]
print(instructoresItagui)

#12. nacidos despues de 2000
nacidos2000 = analisisUsuarios[analisisUsuarios['fecha_nacimiento'] > '2000-01-01']
print(nacidos2000)

#13. nacidos en los 90
nacidos90 = analisisUsuarios[(analisisUsuarios['fecha_nacimiento'] >= '1990-01-01') & 
 (analisisUsuarios['fecha_nacimiento'] < '2000-01-01')]
print(nacidos90)

#14. direcciones en envigado
envigado = analisisUsuarios[analisisUsuarios['direccion'].str.contains('envigado', case=False)]
print(envigado)

#15. especialdiades que empizan por I
empiezanI = analisisUsuarios[analisisUsuarios['especialidad'].str.startswith('I')]
print(empiezanI)

#16. usuarios sin direccion
sinDireccion = analisisUsuarios[analisisUsuarios['direccion'].isnull()]
print(sinDireccion)

#17. usuarios sin especialidad
sinEspecialidad = analisisUsuarios[analisisUsuarios['especialidad'].isnull()]
print(sinEspecialidad)
#18. profesores que viven en sabaneta
docentesSabaneta = analisisUsuarios[(analisisUsuarios['tipo_usuario'] == 'docente') & 
   (analisisUsuarios['direccion'].str.contains('sabaneta', case=False))]
print(docentesSabaneta)


#19. aprendices que viven en bello
aprendicesBello = analisisUsuarios[(analisisUsuarios['tipo_usuario'] == 'aprendiz') & 
  (analisisUsuarios['direccion'].str.contains('bello', case=False))]
print(aprendicesBello)
#20. nacidos en el nuevo milenio
nuevoMilenio = analisisUsuarios[analisisUsuarios['fecha_nacimiento'] >= '2000-01-01']
print(nuevoMilenio)

#1. total por tipo
totalPorTipo=analisisUsuarios.groupby('tipo_usuario').size()
print(totalPorTipo)
#2. total por especialidad
totalporEspecialidad=analisisUsuarios.groupby('especialidad').size()
print(totalporEspecialidad)
#3. cantidad de especialidades distintas
especialidadesDistintas=analisisUsuarios['especialidad'].nunique()
print(especialidadesDistintas)
#4. tipos de usuario por especialidad
tiposUsuarioPorEspecialidad=analisisUsuarios.groupby('especialidad')['tipo_usuario'].value_counts()
print(tiposUsuarioPorEspecialidad)
#5. usuario mas antiguo por tipo
usuarioMasAntiguoPorTipo=analisisUsuarios.groupby('tipo_usuario')['fecha_nacimiento'].min()
print(usuarioMasAntiguoPorTipo)
#6. usuario mas joven por tipo
usuarioMasJovenPorTipo=analisisUsuarios.groupby('tipo_usuario')['fecha_nacimiento'].max()
print(usuarioMasJovenPorTipo)
#7. primer registro por tipo
primerRegistroPorTipo=analisisUsuarios.groupby('tipo_usuario').first()
print(primerRegistroPorTipo)
#8. ultimo registro por tipo
ultimoRegistroPorTipo=analisisUsuarios.groupby('tipo_usuario').last()
print(ultimoRegistroPorTipo)
#9. combinacion tipo por especialidad
combinacionTipoPorEspecialidad=analisisUsuarios.groupby(['tipo_usuario','especialidad']).size()
print(combinacionTipoPorEspecialidad)
#10. el mas viejo por especialidad
masviejoPorEspecialidad=analisisUsuarios.groupby('especialidad')['fecha_nacimiento'].min()
print(masviejoPorEspecialidad)
#11. cuantos de cada especialidad por tipo
cuantporcadaEspecialidadPorTipo=analisisUsuarios.groupby(['especialidad','tipo_usuario']).size()
print(cuantporcadaEspecialidadPorTipo)
#12. edad promedio por tipo
edadPromedioPorTipo=analisisUsuarios.groupby('tipo_usuario')['fecha_nacimiento'].mean()
print(edadPromedioPorTipo)
#13. años de nacimeinto mas frecuente por especialidad
analisisUsuarios['anio'] = pd.to_datetime(analisisUsuarios['fecha_nacimiento']).dt.year
frecuenteAnio = analisisUsuarios.groupby('especialidad')['anio'].agg(lambda x: x.mode()[0])
print(frecuenteAnio)

#14. mes de nacimiento ams frecuente por tipo
analisisUsuarios['mes'] = pd.to_datetime(analisisUsuarios['fecha_nacimiento']).dt.month
frecuenteMes = analisisUsuarios.groupby('tipo_usuario')['mes'].agg(lambda x: x.mode()[0])
print(frecuenteMes)

#15. UNA CONSULTA O FILTRO QUE UD PROPONGA
#Usuarios aprendices cuyo nombre contiene "ana"
anaAprendices = analisisUsuarios[(analisisUsuarios['tipo_usuario'] == 'aprendiz') & 
  (analisisUsuarios['nombre'].str.contains('ana', case=False))]
print(anaAprendices)