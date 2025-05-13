import pandas as pd

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#antes de filtrar como analista de datos debes conocer
#print(dataFrameAsistencia['estado'].unique()) #estratos
#print(dataFrameAsistencia['estrato'].unique()) #estado de asistencia
#print(dataFrameAsistencia['medio_transporte'].unique()) #medio de transporte

#filtros y condiciones para transformar datos
#1. reportar todos los estudiantes que asistieron
estudiantesQueAsistieron=dataFrameAsistencia.query('estado=="asistio"')
print(estudiantesQueAsistieron)
#2. reportar todos los estudiantes que no asistieron
estudiantesQueNoAsistieron=dataFrameAsistencia.query('estado=="no asistio"')
print(estudiantesQueNoAsistieron)
#3. necesito reportar todos los estudiante que llegaron tarde(justificaron)
estudiantesQueLlegaronTarde=dataFrameAsistencia.query('estado=="justificado"')
print(estudiantesQueLlegaronTarde)
#4 necesito reportar  todos los estudiantes de estrato 1
estudiantesEstratoUno=dataFrameAsistencia.query('estrato==1')
print(estudiantesEstratoUno)
#5 necesito reportar todos los estudiantes de estrato alto
estudiantesEstratoAlto=dataFrameAsistencia.query('estrato>=4')
print(estudiantesEstratoAlto)
#6 necesito reportar todos los estudiantes que llegan en metro
estudiantesQueUsanMetro=dataFrameAsistencia.query('medio_transporte=="metro"')
print(estudiantesQueUsanMetro)
#7 necesito reportar todos los estudiantes que llegan en bicicleta
estudiantesQueUsanBicicleta=dataFrameAsistencia.query('medio_transporte=="bicicleta"')
print(estudiantesQueUsanBicicleta)
#8  necesito reportar todos los estudiantes que no caminan para llegar a la u
estudiantesQueNoCaminan=dataFrameAsistencia.query('medio_transporte!="a pie"')
print(estudiantesQueNoCaminan)
#9 reportar todos los registro de asistencia del mes de Abril
estudiantesAbril=dataFrameAsistencia.query('fecha=="2025-04-01" or fecha=="2025-04-02" or fecha=="2025-04-03" or fecha=="2025-04-04" or fecha=="2025-04-05" or fecha=="2025-04-06" or fecha=="2025-04-07" or fecha=="2025-04-08" or fecha=="2025-06-09" or fecha=="2025-04-10"')
print(estudiantesAbril)
#10 reportar todos los estudiantes que faltaron y usa bus para llegar a la u
estudiantesQuefaltanyUsanBus=dataFrameAsistencia.query('medio_transporte=="bus" and estado=="inasistencia"')
print(estudiantesQuefaltanyUsanBus.info())
#11 necesito reportar estudiantes que usan bus son de estrato altos
estudiantesQueUsanBusEstratoAlto=dataFrameAsistencia.query('medio_transporte=="bus" and estrato>=4')
print(estudiantesQueUsanBusEstratoAlto.info())
#12 necesito reportar estudiantes que usan bus son de estrato bajos
estudiantesQueUsanBusEstratoBajo=dataFrameAsistencia.query('medio_transporte=="bus" and estrato<=2')
print(estudiantesQueUsanBusEstratoBajo.info())
#13 reporrtar estudiantes que llegan tarde y son de estrato 2,4,5, o 6
estudiantesQueLlegaronTardeEstrato2_4_5_6=dataFrameAsistencia.query('estado=="justificado" and (estrato==2 or estrato==4 or estrato==5 or estrato==6)')
print(estudiantesQueLlegaronTardeEstrato2_4_5_6.info())
#14 reportar estudantes que usan transportes ecologicos (bicicleta, metro, a pie) y son de estrato 1 o 2
estudiantesQueUsanTransporteEcologico=dataFrameAsistencia.query('estrato<=2 and (medio_transporte=="bicicleta" or medio_transporte=="metro" or medio_transporte=="a pie")')
print(estudiantesQueUsanTransporteEcologico.info())
#15 necesito reportar estudiantes que faltan y usan carro para transportarse
estudiantesQueFaltanYUsanCarro=dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte=="carro"')
print(estudiantesQueFaltanYUsanCarro.info())
#16 reportar estudiantes que asisten son estrato altos y caminan
estudiantesqueAsistenEstratoAltoYCaminar=dataFrameAsistencia.query('estado=="asistio" and estrato>=4 and medio_transporte=="a pie"')
print(estudiantesqueAsistenEstratoAltoYCaminar.info())
#17 reportar estudiante que son estrato bajos y justifican su inasistencia
estudiantesEstratoBajoJustificanInasistencia=dataFrameAsistencia.query('estado=="justificado" and estrato<=2')
print(estudiantesEstratoBajoJustificanInasistencia.info())
#18 reportar estuduantes que son estrato alto y justifican su inasistencia
estudiantesEstratoAltoJustificanInasistencia=dataFrameAsistencia.query('estado=="justificado" and estrato>=4')
print(estudiantesEstratoAltoJustificanInasistencia.info())
#19 reportar estudiantes que usa carro y justifican su inasistencia
estudiantesQueUsanCarroYJustificanInasistencia=dataFrameAsistencia.query('estado=="justificado" and medio_transporte=="carro"')
print(estudiantesQueUsanCarroYJustificanInasistencia.info())
#20 reportar  estudiantes que faltan y usan metro y son estrato medios
estudiantesQueFaltanUsanMetroEstratoMedio=dataFrameAsistencia.query('estado=="inasistencia" and medio_transporte=="metro" and (estrato==3 or estrato==4)')
print(estudiantesQueFaltanUsanMetroEstratoMedio.info())

#agrupaciones y conteos sobre los datos
#1. contar cada registro de asistencia por cada estado
conteoRegistrosPorEstado=dataFrameAsistencia.groupby('estado').size()
print(conteoRegistrosPorEstado)
#2.numero de registro por estrato
conteoRegistrosPorEstrato=dataFrameAsistencia.groupby('estrato').size()
print(conteoRegistrosPorEstrato)
#3. cantidad de estudiantes por medio de transporte
conteoRegistrosPorMedioTransporte=dataFrameAsistencia.groupby('medio_transporte').size()
print(conteoRegistrosPorMedioTransporte)
#4. cantidad de registros por grupo
conteoRegistrosPorGrupo=dataFrameAsistencia.groupby('id_grupo').size()
print(conteoRegistrosPorGrupo)
#5 cruce entre estado y medio de transporte
crucestadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size()
print(crucestadoMedioTransporte)
#6 promedio de estrato por estado de asistencia 
promedioEstratoporEstado=dataFrameAsistencia.groupby('estado')['estrato'].mean()
print(promedioEstratoporEstado)
#7 estrato promedio por medio de transporte
promedioEstratoPorMedioTransporte=dataFrameAsistencia.groupby('medio_transporte')['estrato'].mean()
print(promedioEstratoPorMedioTransporte)
#8 maximo estrato por estado de asistencia
maximoEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].max()
print(maximoEstratoPorEstado)
#9 mininimo estro por estado de asistencia
minimoEstratoPorEstado=dataFrameAsistencia.groupby('estado')['estrato'].min()
#10 conteo de asistencia por grupo y por estado
conteoAsistenciaPorGrupoYEstado=dataFrameAsistencia.groupby(['id_grupo','estado']).size()
print(conteoAsistenciaPorGrupoYEstado)
#11 transporte usados por cada grupo
transporteUsadosPorGrupo=dataFrameAsistencia.groupby(['id_grupo','medio_transporte']).size()
print(transporteUsadosPorGrupo)
#12 cuantos grupos distintos registratron asistencia por fecha
conteoGruposPorFecha=dataFrameAsistencia.groupby(['fecha','id_grupo']).size()
print(conteoGruposPorFecha)
#13 promedio de estrato por fecha
promedioEstratoporEstado=dataFrameAsistencia.groupby('fecha')['estrato'].mean()
print(promedioEstratoporEstado)
# numero de tipo de estado ´por transporte
numeroTipoEstadoPorTransporte=dataFrameAsistencia.groupby(['medio_transporte','estado']).size()
print(numeroTipoEstadoPorTransporte)
#15 primer registro de cada grupo
primerRegistroPorGrupo=dataFrameAsistencia.groupby('id_grupo').first()
print(primerRegistroPorGrupo)
#
#
#
#