webboajustes_db = 'DEV_Ricardo'
webboajustes_db_table = 'TB_BO_AJUSTES_TEST'
webboajustes_maxColNumber = 268
webboajustes_xl_colNameRow = 1
webboajustes_xl_firstDataRow = webboajustes_xl_colNameRow + 1
webboajustes_xl_colCheckFlag = 'A'  # verifica si existe data en esa columna, si no encuentra finaliza el loop de registro de evas
webboajustes_xl_hoja = 'Sheet'  # Nombre de la hoja donde se encuentra la data

webboajustes = [
{'colName': 'ID', 'col': 'A', 'sqlName': 'ID', 'tipo': 'default'},
{'colName': 'FECHA_INICIAL', 'col': 'B', 'sqlName': 'FECHA_INICIAL', 'tipo': 'str_to_datetime_webevas'},
{'colName': 'FECHA_INI', 'col': 'C', 'sqlName': 'FECHA_INI', 'tipo': 'str_to_datetime_webevas'},
{'colName': 'FECHA_FIN', 'col': 'D', 'sqlName': 'FECHA_FIN', 'tipo': 'str_to_datetime_webevas'},
{'colName': 'CBO_ESTADO', 'col': 'E', 'sqlName': 'CBO_ESTADO', 'tipo': 'default'},
{'colName': 'NIVEL_1', 'col': 'F', 'sqlName': 'NIVEL_1', 'tipo': 'default'},
{'colName': 'NIVEL_2', 'col': 'G', 'sqlName': 'NIVEL_2', 'tipo': 'default'},
{'colName': 'NIVEL_3', 'col': 'H', 'sqlName': 'NIVEL_3', 'tipo': 'default'},
{'colName': 'NIVEL_4', 'col': 'I', 'sqlName': 'NIVEL_4', 'tipo': 'default'},
{'colName': 'NIVEL_5', 'col': 'J', 'sqlName': 'NIVEL_5', 'tipo': 'default'},
{'colName': 'TXT_OBSERVACION', 'col': 'K', 'sqlName': 'TXT_OBSERVACION', 'tipo': 'default'},
{'colName': 'DNI_USUARIO', 'col': 'L', 'sqlName': 'DNI_USUARIO', 'tipo': 'default'},
{'colName': 'DNI_AGENTE', 'col': 'M', 'sqlName': 'DNI_AGENTE', 'tipo': 'default'},
{'colName': 'IDGestion', 'col': 'N', 'sqlName': 'IDGestion', 'tipo': 'default'},
{'colName': 'FechaMonitoreo', 'col': 'O', 'sqlName': 'FechaMonitoreo', 'tipo': 'default'},
{'colName': 'TipoMonitoreo', 'col': 'P', 'sqlName': 'TipoMonitoreo', 'tipo': 'default'},
{'colName': 'FechaAjuste', 'col': 'Q', 'sqlName': 'FechaAjuste', 'tipo': 'default'},
{'colName': 'HoraAjuste', 'col': 'R', 'sqlName': 'HoraAjuste', 'tipo': 'default'},
{'colName': 'NumeroTelefonico', 'col': 'S', 'sqlName': 'NumeroTelefonico', 'tipo': 'default'},
{'colName': 'NumeroCaso', 'col': 'T', 'sqlName': 'NumeroCaso', 'tipo': 'default'},
{'colName': 'TxtDescripcionAjuste', 'col': 'U', 'sqlName': 'TxtDescripcionAjuste', 'tipo': 'default'},
{'colName': 'TxtOBSERVACIONES', 'col': 'V', 'sqlName': 'TxtOBSERVACIONES', 'tipo': 'default'},
{'colName': 'CAMPO_1_1', 'col': 'W', 'sqlName': 'CAMPO_1_1', 'tipo': 'default'},
{'colName': 'CAMPO_1_2', 'col': 'X', 'sqlName': 'CAMPO_1_2', 'tipo': 'default'},
{'colName': 'CAMPO_1_3', 'col': 'Y', 'sqlName': 'CAMPO_1_3', 'tipo': 'default'},
{'colName': 'STATUS', 'col': 'Z', 'sqlName': 'STATUS', 'tipo': 'default'},
{'colName': 'TXT_PEDIDO_ASOCIADO', 'col': 'AA', 'sqlName': 'TXT_PEDIDO_ASOCIADO', 'tipo': 'default'},
{'colName': 'ID_CARGA', 'col': 'AB', 'sqlName': 'ID_CARGA', 'tipo': 'default'},
{'colName': 'AGENTE', 'col': 'AC', 'sqlName': 'USUARIO', 'tipo': 'default'},

]
