webboatc_db = 'DEV_Ricardo'
webboatc_db_table = 'TB_BO_ATC_TEST'
webboatc_maxColNumber = 60
webboatc_xl_colNameRow = 1
webboatc_xl_firstDataRow = webboatc_xl_colNameRow + 1
webboatc_xl_colCheckFlag = 'A'  # verifica si existe data en esa columna, si no encuentra finaliza el loop de registro de evas
webboatc_xl_hoja = 'Sheet'  # Nombre de la hoja donde se encuentra la data

webboatc = [
    {'colName': 'ID', 'col': 'A', 'sqlName': 'ID', 'tipo': 'default'},
    {'colName': 'SN', 'col': 'B', 'sqlName': 'SN', 'tipo': 'default'},
    {'colName': 'FECHA_INICIAL', 'col': 'C', 'sqlName': 'FECHA_INICIAL', 'tipo': 'str_to_datetime_webevas'},
    {'colName': 'FECHA_INI', 'col': 'D', 'sqlName': 'FECHA_INI', 'tipo': 'str_to_datetime_webevas'},
    {'colName': 'FECHA_FIN', 'col': 'E', 'sqlName': 'FECHA_FIN', 'tipo': 'str_to_datetime_webevas'},
    {'colName': 'CBO_ESTADO', 'col': 'G', 'sqlName': 'CBO_ESTADO', 'tipo': 'default'},
    {'colName': 'NIVEL_1', 'col': 'H', 'sqlName': 'NIVEL_1', 'tipo': 'default'},
    {'colName': 'NIVEL_2', 'col': 'I', 'sqlName': 'NIVEL_2', 'tipo': 'default'},
    {'colName': 'NIVEL_3', 'col': 'J', 'sqlName': 'NIVEL_3', 'tipo': 'default'},
    {'colName': 'NIVEL_4', 'col': 'K', 'sqlName': 'NIVEL_4', 'tipo': 'default'},
    {'colName': 'NIVEL_5', 'col': 'L', 'sqlName': 'NIVEL_5', 'tipo': 'default'},
    {'colName': 'TXT_OBSERVACION', 'col': 'M', 'sqlName': 'TXT_OBSERVACION', 'tipo': 'default'},
    {'colName': 'DNI_USUARIO', 'col': 'N', 'sqlName': 'DNI_USUARIO', 'tipo': 'default'},
    {'colName': 'ESTADO', 'col': 'Q', 'sqlName': 'ESTADO', 'tipo': 'default'},
    {'colName': 'TIPO_FALLA', 'col': 'R', 'sqlName': 'TIPO_FALLA', 'tipo': 'default'},
    {'colName': 'MOTIVO_FALLA', 'col': 'S', 'sqlName': 'MOTIVO_FALLA', 'tipo': 'default'},
    {'colName': 'DNI_AGENTE', 'col': 'T', 'sqlName': 'DNI_AGENTE', 'tipo': 'default'},
    {'colName': 'ID_GESTION', 'col': 'U', 'sqlName': 'ID_GESTION', 'tipo': 'default'},
    {'colName': 'FECHA_LLAMADA', 'col': 'V', 'sqlName': 'FECHA_LLAMADA', 'tipo': 'default'},
    {'colName': 'TMO', 'col': 'W', 'sqlName': 'TMO', 'tipo': 'default'},
    {'colName': 'NOMBRE_CLIENTE', 'col': 'X', 'sqlName': 'NOMBRE_CLIENTE', 'tipo': 'default'},
    {'colName': 'NUMERO_LLAMANTE', 'col': 'Y', 'sqlName': 'NUMERO_LLAMANTE', 'tipo': 'default'},
    {'colName': 'TIPO_MONITOREO', 'col': 'Z', 'sqlName': 'TIPO_MONITOREO', 'tipo': 'default'},
    {'colName': 'CAMPO_2_1', 'col': 'AA', 'sqlName': 'CAMPO_2_1', 'tipo': 'default'},
    {'colName': 'CAMPO_2_1_CB', 'col': 'AB', 'sqlName': 'CAMPO_2_1_CB', 'tipo': 'default'},
    {'colName': 'CAMPO_2_1_MP', 'col': 'AC', 'sqlName': 'CAMPO_2_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_2_2', 'col': 'AD', 'sqlName': 'CAMPO_2_2', 'tipo': 'default'},
    {'colName': 'CAMPO_2_2_CB', 'col': 'AE', 'sqlName': 'CAMPO_2_2_CB', 'tipo': 'default'},
    {'colName': 'CAMPO_2_2_MP', 'col': 'AF', 'sqlName': 'CAMPO_2_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_2_3', 'col': 'AG', 'sqlName': 'CAMPO_2_3', 'tipo': 'default'},
    {'colName': 'CAMPO_2_3_CB', 'col': 'AH', 'sqlName': 'CAMPO_2_3_CB', 'tipo': 'default'},
    {'colName': 'CAMPO_2_3_MP', 'col': 'AI', 'sqlName': 'CAMPO_2_3_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_3_1', 'col': 'AJ', 'sqlName': 'CAMPO_3_1', 'tipo': 'default'},
    {'colName': 'CAMPO_3_1_CB', 'col': 'AK', 'sqlName': 'CAMPO_3_1_CB', 'tipo': 'default'},
    {'colName': 'CAMPO_3_1_MP', 'col': 'AL', 'sqlName': 'CAMPO_3_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_4_1', 'col': 'AM', 'sqlName': 'CAMPO_4_1', 'tipo': 'default'},
    {'colName': 'CAMPO_4_1_CB', 'col': 'AN', 'sqlName': 'CAMPO_4_1_CB', 'tipo': 'default'},
    {'colName': 'CAMPO_4_1_MP', 'col': 'AO', 'sqlName': 'CAMPO_4_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_4_2', 'col': 'AP', 'sqlName': 'CAMPO_4_2', 'tipo': 'default'},
    {'colName': 'CAMPO_4_2_CB', 'col': 'AQ', 'sqlName': 'CAMPO_4_2_CB', 'tipo': 'default'},
    {'colName': 'CAMPO_4_2_MP', 'col': 'AR', 'sqlName': 'CAMPO_4_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_4_3', 'col': 'AS', 'sqlName': 'CAMPO_4_3', 'tipo': 'default'},
    {'colName': 'CAMPO_4_3_CB', 'col': 'AT', 'sqlName': 'CAMPO_4_3_CB', 'tipo': 'default'},
    {'colName': 'CAMPO_4_3_MP', 'col': 'AU', 'sqlName': 'CAMPO_4_3_MP', 'tipo': 'default'},
    {'colName': 'DESCRIPCION_LLAMADA', 'col': 'AV', 'sqlName': 'DESCRIPCION_LLAMADA', 'tipo': 'default'},
    {'colName': 'RECOMENDACIONES', 'col': 'AW', 'sqlName': 'RECOMENDACIONES', 'tipo': 'default'},
    {'colName': 'AGENTE', 'col': 'AX', 'sqlName': 'USUARIO', 'tipo': 'default'}
]
