fb_db = 'DB_FEEDBACK'
fb_db_table = 'FEEDBACK_DEV'  # 'FEEDBACK_DEV'
fb_maxColNumber = 30
fb_xl_colNameRow = 1
fb_xl_firstDataRow = fb_xl_colNameRow + 1
fb_xl_colCheckFlag = 'C'  # verifica si existe data en esa columna, si no encuentra finaliza el loop de registro de evas
fb_xl_hoja = 'Pag1'  # Nombre de la hoja donde se encuentra la data

fb = [
    {'colName': 'Id_incidenciaOpera', 'col': 'C', 'sqlName': 'Id_incidenciaOpera', 'tipo': 'default'},
    {'colName': 'Personal', 'col': 'D', 'sqlName': 'Personal', 'tipo': 'default'},
    {'colName': 'NombreCampana', 'col': 'E', 'sqlName': 'NombreCampana', 'tipo': 'default'},
    {'colName': 'NombreSubCampana', 'col': 'F', 'sqlName': 'NombreSubCampana', 'tipo': 'default'},
    {'colName': 'NombreAtributoPenalizado', 'col': 'G', 'sqlName': 'NombreAtributoPenalizado', 'tipo': 'default'},
    {'colName': 'Nombretematica', 'col': 'H', 'sqlName': 'Nombretematica', 'tipo': 'default'},
    {'colName': 'Incidencia_detectada', 'col': 'I', 'sqlName': 'Incidencia_detectada', 'tipo': 'default'},
    {'colName': 'FechaIncidencia', 'col': 'J', 'sqlName': 'FechaIncidencia', 'tipo': 'xl_date'},
    {'colName': 'FechaDeteccion', 'col': 'K', 'sqlName': 'FechaDeteccion', 'tipo': 'xl_date'},
    {'colName': 'FormaSolucion', 'col': 'L', 'sqlName': 'FormaSolucion', 'tipo': 'default'},
    {'colName': 'Aceptacion_Feedback', 'col': 'M', 'sqlName': 'Aceptacion_Feedback', 'tipo': 'default'},
    {'colName': 'Recepcion_feedback', 'col': 'N', 'sqlName': 'Recepcion_feedback', 'tipo': 'str_to_datetime'},
    {'colName': 'Compromiso_Mejora', 'col': 'O', 'sqlName': 'Compromiso_Mejora', 'tipo': 'default'},
    {'colName': 'descripcion', 'col': 'P', 'sqlName': 'descripcion', 'tipo': 'default'},
    {'colName': 'Ejecutivo_Calidad', 'col': 'Q', 'sqlName': 'Ejecutivo_Calidad', 'tipo': 'default'},
    {'colName': 'SancionOperaciones', 'col': 'R', 'sqlName': 'SancionOperaciones', 'tipo': 'default'},
    {'colName': 'ObservacionOperacion', 'col': 'S', 'sqlName': 'ObservacionOperacion', 'tipo': 'default'},
    {'colName': 'IdSugerenciaRespCalidad', 'col': 'T', 'sqlName': 'IdSugerenciaRespCalidad', 'tipo': 'default'},
    {'colName': 'SUPERVISOR', 'col': 'U', 'sqlName': 'SUPERVISOR', 'tipo': 'default'},
    {'colName': 'RESPONSABLE', 'col': 'V', 'sqlName': 'RESPONSABLE', 'tipo': 'default'},
    {'colName': 'GERENTE', 'col': 'W', 'sqlName': 'GERENTE', 'tipo': 'default'},
    {'colName': 'Id_llamada', 'col': 'X', 'sqlName': 'Id_llamada', 'tipo': 'default'},
    {'colName': 'telefono', 'col': 'Y', 'sqlName': 'telefono', 'tipo': 'default'},
    {'colName': 'Antiguedad', 'col': 'Z', 'sqlName': 'Antiguedad', 'tipo': 'default'},
    {'colName': 'AtributoPenalizado', 'col': 'AA', 'sqlName': 'AtributoPenalizado', 'tipo': 'default'},
    {'colName': 'REGISTRO', 'col': 'AB', 'sqlName': 'REGISTRO', 'tipo': 'default'}
]
