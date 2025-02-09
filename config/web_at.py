webat_db = 'DEV_Ricardo'
webat_db_table = 'TB_AT_TEST'
webat_maxColNumber = 187
webat_xl_colNameRow = 1
webat_xl_firstDataRow = webat_xl_colNameRow + 1
webat_xl_colCheckFlag = 'A'  # verifica si existe data en esa columna, si no encuentra finaliza el loop de registro de evas
webat_xl_hoja = 'Sheet'  # Nombre de la hoja donde se encuentra la data

webat = [
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
    {'colName': 'ID_CARGA', 'col': 'O', 'sqlName': 'ID_CARGA', 'tipo': 'default'},
    {'colName': 'TXT_PEDIDO_ASOCIADO', 'col': 'P', 'sqlName': 'TXT_PEDIDO_ASOCIADO', 'tipo': 'default'},
    {'colName': 'CODIGO_ASESOR', 'col': 'Q', 'sqlName': 'CODIGO_ASESOR', 'tipo': 'default'},
    {'colName': 'NOMBRE_ASESOR', 'col': 'R', 'sqlName': 'NOMBRE_ASESOR', 'tipo': 'default'},
    {'colName': 'FECHA_LLAMADA', 'col': 'S', 'sqlName': 'FECHA_LLAMADA', 'tipo': 'default'},
    {'colName': 'HORA_LLAMADA', 'col': 'T', 'sqlName': 'HORA_LLAMADA', 'tipo': 'default'},
    {'colName': 'TMO', 'col': 'U', 'sqlName': 'TMO', 'tipo': 'default'},
    {'colName': 'NOMBRE_CLIENTE', 'col': 'V', 'sqlName': 'NOMBRE_CLIENTE', 'tipo': 'default'},
    {'colName': 'NRO_MSISDN', 'col': 'W', 'sqlName': 'NRO_MSISDN', 'tipo': 'default'},
    {'colName': 'NRO_CONSULTA', 'col': 'X', 'sqlName': 'NRO_CONSULTA', 'tipo': 'default'},
    {'colName': 'TIPO_LLAMADA', 'col': 'Y', 'sqlName': 'TIPO_LLAMADA', 'tipo': 'default'},
    {'colName': 'MOTIVO_CONSULTA', 'col': 'Z', 'sqlName': 'MOTIVO_CONSULTA', 'tipo': 'default'},
    {'colName': 'DESCRIPCION_LLAMADA', 'col': 'AA', 'sqlName': 'DESCRIPCION_LLAMADA', 'tipo': 'default'},
    {'colName': 'CAMPO_1_1', 'col': 'AB', 'sqlName': 'CAMPO_1_1', 'tipo': 'default'},
    {'colName': 'CAMPO_1_1_MP', 'col': 'AC', 'sqlName': 'CAMPO_1_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_1_2', 'col': 'AD', 'sqlName': 'CAMPO_1_2', 'tipo': 'default'},
    {'colName': 'CAMPO_1_2_MP', 'col': 'AE', 'sqlName': 'CAMPO_1_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_1_3', 'col': 'AF', 'sqlName': 'CAMPO_1_3', 'tipo': 'default'},
    {'colName': 'CAMPO_1_3_MP', 'col': 'AG', 'sqlName': 'CAMPO_1_3_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_2_1', 'col': 'AH', 'sqlName': 'CAMPO_2_1', 'tipo': 'default'},
    {'colName': 'CAMPO_2_1_MP', 'col': 'AI', 'sqlName': 'CAMPO_2_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_2_2', 'col': 'AJ', 'sqlName': 'CAMPO_2_2', 'tipo': 'default'},
    {'colName': 'CAMPO_2_2_MP', 'col': 'AK', 'sqlName': 'CAMPO_2_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_3_1', 'col': 'AL', 'sqlName': 'CAMPO_3_1', 'tipo': 'default'},
    {'colName': 'CAMPO_3_1_MP', 'col': 'AM', 'sqlName': 'CAMPO_3_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_3_2', 'col': 'AN', 'sqlName': 'CAMPO_3_2', 'tipo': 'default'},
    {'colName': 'CAMPO_3_2_MP', 'col': 'AO', 'sqlName': 'CAMPO_3_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_3_3', 'col': 'AP', 'sqlName': 'CAMPO_3_3', 'tipo': 'default'},
    {'colName': 'CAMPO_3_3_MP', 'col': 'AQ', 'sqlName': 'CAMPO_3_3_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_4_1', 'col': 'AR', 'sqlName': 'CAMPO_4_1', 'tipo': 'default'},
    {'colName': 'CAMPO_4_1_MP', 'col': 'AS', 'sqlName': 'CAMPO_4_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_4_1_1', 'col': 'AT', 'sqlName': 'CAMPO_4_1_1', 'tipo': 'default'},
    {'colName': 'CAMPO_4_1_1_MP', 'col': 'AU', 'sqlName': 'CAMPO_4_1_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_4_2', 'col': 'AV', 'sqlName': 'CAMPO_4_2', 'tipo': 'default'},
    {'colName': 'CAMPO_4_2_MP', 'col': 'AW', 'sqlName': 'CAMPO_4_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_4_2_1', 'col': 'AX', 'sqlName': 'CAMPO_4_2_1', 'tipo': 'default'},
    {'colName': 'CAMPO_4_2_1_MP', 'col': 'AY', 'sqlName': 'CAMPO_4_2_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_4_2_2', 'col': 'AZ', 'sqlName': 'CAMPO_4_2_2', 'tipo': 'default'},
    {'colName': 'CAMPO_4_2_2_MP', 'col': 'BA', 'sqlName': 'CAMPO_4_2_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_5_1', 'col': 'BB', 'sqlName': 'CAMPO_5_1', 'tipo': 'default'},
    {'colName': 'CAMPO_5_1_MP', 'col': 'BC', 'sqlName': 'CAMPO_5_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_5_2', 'col': 'BD', 'sqlName': 'CAMPO_5_2', 'tipo': 'default'},
    {'colName': 'CAMPO_5_2_MP', 'col': 'BE', 'sqlName': 'CAMPO_5_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_5_3', 'col': 'BF', 'sqlName': 'CAMPO_5_3', 'tipo': 'default'},
    {'colName': 'CAMPO_5_3_MP', 'col': 'BG', 'sqlName': 'CAMPO_5_3_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_5_4', 'col': 'BH', 'sqlName': 'CAMPO_5_4', 'tipo': 'default'},
    {'colName': 'CAMPO_5_4_MP', 'col': 'BI', 'sqlName': 'CAMPO_5_4_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_5_5', 'col': 'BJ', 'sqlName': 'CAMPO_5_5', 'tipo': 'default'},
    {'colName': 'CAMPO_5_5_MP', 'col': 'BK', 'sqlName': 'CAMPO_5_5_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_5_6', 'col': 'BL', 'sqlName': 'CAMPO_5_6', 'tipo': 'default'},
    {'colName': 'CAMPO_5_6_MP', 'col': 'BM', 'sqlName': 'CAMPO_5_6_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_5_7', 'col': 'BN', 'sqlName': 'CAMPO_5_7', 'tipo': 'default'},
    {'colName': 'CAMPO_5_7_MP', 'col': 'BO', 'sqlName': 'CAMPO_5_7_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_6_1', 'col': 'BP', 'sqlName': 'CAMPO_6_1', 'tipo': 'default'},
    {'colName': 'CAMPO_6_1_MP', 'col': 'BQ', 'sqlName': 'CAMPO_6_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_1', 'col': 'BR', 'sqlName': 'CAMPO_7_1', 'tipo': 'default'},
    {'colName': 'CAMPO_7_1_MP', 'col': 'BS', 'sqlName': 'CAMPO_7_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_2', 'col': 'BT', 'sqlName': 'CAMPO_7_2', 'tipo': 'default'},
    {'colName': 'CAMPO_7_2_MP', 'col': 'BU', 'sqlName': 'CAMPO_7_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_3', 'col': 'BV', 'sqlName': 'CAMPO_7_3', 'tipo': 'default'},
    {'colName': 'CAMPO_7_3_MP', 'col': 'BW', 'sqlName': 'CAMPO_7_3_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_4', 'col': 'BX', 'sqlName': 'CAMPO_7_4', 'tipo': 'default'},
    {'colName': 'CAMPO_7_4_MP', 'col': 'BY', 'sqlName': 'CAMPO_7_4_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_5', 'col': 'BZ', 'sqlName': 'CAMPO_7_5', 'tipo': 'default'},
    {'colName': 'CAMPO_7_5_MP', 'col': 'CA', 'sqlName': 'CAMPO_7_5_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_6', 'col': 'CB', 'sqlName': 'CAMPO_7_6', 'tipo': 'default'},
    {'colName': 'CAMPO_7_6_MP', 'col': 'CC', 'sqlName': 'CAMPO_7_6_MP', 'tipo': 'default'},
    {'colName': 'TIPIFICACION_SIAC', 'col': 'CD', 'sqlName': 'TIPIFICACION_SIAC', 'tipo': 'default'},
    {'colName': 'REINCIDENCIA', 'col': 'CE', 'sqlName': 'REINCIDENCIA', 'tipo': 'default'},
    {'colName': 'USO_CES', 'col': 'CF', 'sqlName': 'USO_CES', 'tipo': 'default'},
    {'colName': 'USO_SUIC', 'col': 'CG', 'sqlName': 'USO_SUIC', 'tipo': 'default'},
    {'colName': 'AJUSTE_INDEBIDO', 'col': 'CH', 'sqlName': 'AJUSTE_INDEBIDO', 'tipo': 'default'},
    {'colName': 'ALERTA_DICCION', 'col': 'CI', 'sqlName': 'ALERTA_DICCION', 'tipo': 'default'},
    {'colName': 'CAMPO_4_1_2', 'col': 'CJ', 'sqlName': 'CAMPO_4_1_2', 'tipo': 'default'},
    {'colName': 'CAMPO_4_1_2_MP', 'col': 'CK', 'sqlName': 'CAMPO_4_1_2_MP', 'tipo': 'default'},
    {'colName': 'CBO_INDICO', 'col': 'CL', 'sqlName': 'CBO_INDICO', 'tipo': 'default'},
    {'colName': 'CBO_PIDIO', 'col': 'CM', 'sqlName': 'CBO_PIDIO', 'tipo': 'default'},
    {'colName': 'TXT_RECOMIENDA_FIDE', 'col': 'CN', 'sqlName': 'TXT_RECOMIENDA_FIDE', 'tipo': 'default'},
    {'colName': 'TXT_RECOMIENDA_COME', 'col': 'CO', 'sqlName': 'TXT_RECOMIENDA_COME', 'tipo': 'default'},
    {'colName': 'TXT_OBSER_RECOMEN', 'col': 'CP', 'sqlName': 'TXT_OBSER_RECOMEN', 'tipo': 'default'},
    {'colName': 'cbo_Sub_Motivo', 'col': 'CQ', 'sqlName': 'cbo_Sub_Motivo', 'tipo': 'default'},
    {'colName': 'TxtServicioAfectado', 'col': 'CR', 'sqlName': 'TxtServicioAfectado', 'tipo': 'default'},
    {'colName': 'TxtDetalleAgente', 'col': 'CS', 'sqlName': 'TxtDetalleAgente', 'tipo': 'default'},
    {'colName': 'CBO_ESTADO_1', 'col': 'CT', 'sqlName': 'CBO_ESTADO_1', 'tipo': 'default'},
    {'colName': 'cbo_Sub_Motivo_1', 'col': 'CU', 'sqlName': 'cbo_Sub_Motivo_1', 'tipo': 'default'},
    {'colName': 'CBO_ALERTA_POSIBLE', 'col': 'CV', 'sqlName': 'CBO_ALERTA_POSIBLE', 'tipo': 'default'},
    {'colName': 'CBO_ASESOR_CONTABA', 'col': 'CW', 'sqlName': 'CBO_ASESOR_CONTABA', 'tipo': 'default'},
    {'colName': 'CAMPO_1_1_3', 'col': 'CX', 'sqlName': 'CAMPO_1_1_3', 'tipo': 'default'},
    {'colName': 'CAMPO_1_1_3_MP', 'col': 'CY', 'sqlName': 'CAMPO_1_1_3_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_1_1_4', 'col': 'CZ', 'sqlName': 'CAMPO_1_1_4', 'tipo': 'default'},
    {'colName': 'CAMPO_1_1_4_MP', 'col': 'DA', 'sqlName': 'CAMPO_1_1_4_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_1_1_5', 'col': 'DB', 'sqlName': 'CAMPO_1_1_5', 'tipo': 'default'},
    {'colName': 'CAMPO_1_1_5_MP', 'col': 'DC', 'sqlName': 'CAMPO_1_1_5_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_1_1_6', 'col': 'DD', 'sqlName': 'CAMPO_1_1_6', 'tipo': 'default'},
    {'colName': 'CAMPO_1_1_6_MP', 'col': 'DE', 'sqlName': 'CAMPO_1_1_6_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_2_1_2', 'col': 'DF', 'sqlName': 'CAMPO_2_1_2', 'tipo': 'default'},
    {'colName': 'CAMPO_2_1_2_MP', 'col': 'DG', 'sqlName': 'CAMPO_2_1_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_2_3', 'col': 'DH', 'sqlName': 'CAMPO_2_3', 'tipo': 'default'},
    {'colName': 'CAMPO_2_3_MP', 'col': 'DI', 'sqlName': 'CAMPO_2_3_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_2_3_1', 'col': 'DJ', 'sqlName': 'CAMPO_2_3_1', 'tipo': 'default'},
    {'colName': 'CAMPO_2_3_1_MP', 'col': 'DK', 'sqlName': 'CAMPO_2_3_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_2_3_2', 'col': 'DL', 'sqlName': 'CAMPO_2_3_2', 'tipo': 'default'},
    {'colName': 'CAMPO_2_3_2_MP', 'col': 'DM', 'sqlName': 'CAMPO_2_3_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_2_3_3', 'col': 'DN', 'sqlName': 'CAMPO_2_3_3', 'tipo': 'default'},
    {'colName': 'CAMPO_2_3_3_MP', 'col': 'DO', 'sqlName': 'CAMPO_2_3_3_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_2_4', 'col': 'DP', 'sqlName': 'CAMPO_2_4', 'tipo': 'default'},
    {'colName': 'CAMPO_2_4_MP', 'col': 'DQ', 'sqlName': 'CAMPO_2_4_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_2_4_1', 'col': 'DR', 'sqlName': 'CAMPO_2_4_1', 'tipo': 'default'},
    {'colName': 'CAMPO_2_4_1_MP', 'col': 'DS', 'sqlName': 'CAMPO_2_4_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_2_4_2', 'col': 'DT', 'sqlName': 'CAMPO_2_4_2', 'tipo': 'default'},
    {'colName': 'CAMPO_2_4_2_MP', 'col': 'DU', 'sqlName': 'CAMPO_2_4_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_3_1_MP_2', 'col': 'DV', 'sqlName': 'CAMPO_3_1_MP_2', 'tipo': 'default'},
    {'colName': 'CAMPO_3_2_1', 'col': 'DW', 'sqlName': 'CAMPO_3_2_1', 'tipo': 'default'},
    {'colName': 'CAMPO_3_2_1_MP', 'col': 'DX', 'sqlName': 'CAMPO_3_2_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_3_2_1_MP_2', 'col': 'DY', 'sqlName': 'CAMPO_3_2_1_MP_2', 'tipo': 'default'},
    {'colName': 'CAMPO_3_2_2', 'col': 'DZ', 'sqlName': 'CAMPO_3_2_2', 'tipo': 'default'},
    {'colName': 'CAMPO_3_2_2_MP', 'col': 'EA', 'sqlName': 'CAMPO_3_2_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_3_2_2_MP_2', 'col': 'EB', 'sqlName': 'CAMPO_3_2_2_MP_2', 'tipo': 'default'},
    {'colName': 'CAMPO_3_3_1', 'col': 'EC', 'sqlName': 'CAMPO_3_3_1', 'tipo': 'default'},
    {'colName': 'CAMPO_3_3_1_MP', 'col': 'ED', 'sqlName': 'CAMPO_3_3_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_3_3_2', 'col': 'EE', 'sqlName': 'CAMPO_3_3_2', 'tipo': 'default'},
    {'colName': 'CAMPO_3_3_2_MP', 'col': 'EF', 'sqlName': 'CAMPO_3_3_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_3_3_3', 'col': 'EG', 'sqlName': 'CAMPO_3_3_3', 'tipo': 'default'},
    {'colName': 'CAMPO_3_3_3_MP', 'col': 'EH', 'sqlName': 'CAMPO_3_3_3_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_6_2', 'col': 'EI', 'sqlName': 'CAMPO_6_2', 'tipo': 'default'},
    {'colName': 'CAMPO_6_2_MP', 'col': 'EJ', 'sqlName': 'CAMPO_6_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_6_2_1', 'col': 'EK', 'sqlName': 'CAMPO_6_2_1', 'tipo': 'default'},
    {'colName': 'CAMPO_6_2_1_MP', 'col': 'EL', 'sqlName': 'CAMPO_6_2_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_6_3', 'col': 'EM', 'sqlName': 'CAMPO_6_3', 'tipo': 'default'},
    {'colName': 'CAMPO_6_3_MP', 'col': 'EN', 'sqlName': 'CAMPO_6_3_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_6_4', 'col': 'EO', 'sqlName': 'CAMPO_6_4', 'tipo': 'default'},
    {'colName': 'CAMPO_6_4_MP', 'col': 'EP', 'sqlName': 'CAMPO_6_4_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_2_1', 'col': 'EQ', 'sqlName': 'CAMPO_7_2_1', 'tipo': 'default'},
    {'colName': 'CAMPO_7_2_1_MP', 'col': 'ER', 'sqlName': 'CAMPO_7_2_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_2_2', 'col': 'ES', 'sqlName': 'CAMPO_7_2_2', 'tipo': 'default'},
    {'colName': 'CAMPO_7_2_2_MP', 'col': 'ET', 'sqlName': 'CAMPO_7_2_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_5_1', 'col': 'EU', 'sqlName': 'CAMPO_7_5_1', 'tipo': 'default'},
    {'colName': 'CAMPO_7_5_1_MP', 'col': 'EV', 'sqlName': 'CAMPO_7_5_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_5_2', 'col': 'EW', 'sqlName': 'CAMPO_7_5_2', 'tipo': 'default'},
    {'colName': 'CAMPO_7_5_2_MP', 'col': 'EX', 'sqlName': 'CAMPO_7_5_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_6_1', 'col': 'EY', 'sqlName': 'CAMPO_7_6_1', 'tipo': 'default'},
    {'colName': 'CAMPO_7_6_1_MP', 'col': 'EZ', 'sqlName': 'CAMPO_7_6_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_6_2', 'col': 'FA', 'sqlName': 'CAMPO_7_6_2', 'tipo': 'default'},
    {'colName': 'CAMPO_7_6_2_MP', 'col': 'FB', 'sqlName': 'CAMPO_7_6_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_6_3', 'col': 'FC', 'sqlName': 'CAMPO_7_6_3', 'tipo': 'default'},
    {'colName': 'CAMPO_7_6_3_MP', 'col': 'FD', 'sqlName': 'CAMPO_7_6_3_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_7', 'col': 'FE', 'sqlName': 'CAMPO_7_7', 'tipo': 'default'},
    {'colName': 'CAMPO_7_7_MP', 'col': 'FF', 'sqlName': 'CAMPO_7_7_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_7_1', 'col': 'FG', 'sqlName': 'CAMPO_7_7_1', 'tipo': 'default'},
    {'colName': 'CAMPO_7_7_1_MP', 'col': 'FH', 'sqlName': 'CAMPO_7_7_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_7_2', 'col': 'FI', 'sqlName': 'CAMPO_7_7_2', 'tipo': 'default'},
    {'colName': 'CAMPO_7_7_2_MP', 'col': 'FJ', 'sqlName': 'CAMPO_7_7_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_7_8', 'col': 'FK', 'sqlName': 'CAMPO_7_8', 'tipo': 'default'},
    {'colName': 'CAMPO_7_8_MP', 'col': 'FL', 'sqlName': 'CAMPO_7_8_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_8_1', 'col': 'FM', 'sqlName': 'CAMPO_8_1', 'tipo': 'default'},
    {'colName': 'CAMPO_8_1_MP', 'col': 'FN', 'sqlName': 'CAMPO_8_1_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_8_2', 'col': 'FO', 'sqlName': 'CAMPO_8_2', 'tipo': 'default'},
    {'colName': 'CAMPO_8_2_MP', 'col': 'FP', 'sqlName': 'CAMPO_8_2_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_8_3', 'col': 'FQ', 'sqlName': 'CAMPO_8_3', 'tipo': 'default'},
    {'colName': 'CAMPO_8_3_MP', 'col': 'FR', 'sqlName': 'CAMPO_8_3_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_8_4', 'col': 'FS', 'sqlName': 'CAMPO_8_4', 'tipo': 'default'},
    {'colName': 'CAMPO_8_4_MP', 'col': 'FT', 'sqlName': 'CAMPO_8_4_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_8_5', 'col': 'FU', 'sqlName': 'CAMPO_8_5', 'tipo': 'default'},
    {'colName': 'CAMPO_8_5_MP', 'col': 'FV', 'sqlName': 'CAMPO_8_5_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_8_6', 'col': 'FW', 'sqlName': 'CAMPO_8_6', 'tipo': 'default'},
    {'colName': 'CAMPO_8_6_MP', 'col': 'FX', 'sqlName': 'CAMPO_8_6_MP', 'tipo': 'default'},
    {'colName': 'CAMPO_8_7', 'col': 'FY', 'sqlName': 'CAMPO_8_7', 'tipo': 'default'},
    {'colName': 'CAMPO_8_7_MP', 'col': 'FZ', 'sqlName': 'CAMPO_8_7_MP', 'tipo': 'default'},
    {'colName': 'TMO_MONITOREO', 'col': 'GA', 'sqlName': 'TMO_MONITOREO', 'tipo': 'default'},
    {'colName': 'SatifaccionAtencion', 'col': 'GB', 'sqlName': 'SatifaccionAtencion', 'tipo': 'default'},
    {'colName': 'TxtSugerenciaProceso', 'col': 'GC', 'sqlName': 'TxtSugerenciaProceso', 'tipo': 'default'},
    {'colName': 'GRABACION', 'col': 'GD', 'sqlName': 'GRABACION', 'tipo': 'default'},
    {'colName': 'AGENTE', 'col': 'GE', 'sqlName': 'USUARIO', 'tipo': 'default'}
]
