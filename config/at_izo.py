at_izo_db = 'CLARO_IN_CALIDAD_AT'
at_izo_db_table = 'DEV_IZO'  # 'TEMP_IZO'
at_izo_maxColNumber = 130
at_izo_xl_colNameRow = 4
at_izo_xl_firstDataRow = at_izo_xl_colNameRow + 1
at_izo_xl_colCheckFlag = 'A'  # verifica si existe data en esa columna, si no encuentra finaliza el loop de registro de evas
at_izo_xl_hoja = 'DATA'  # Nombre de la hoja donde se encuentra la data

at_izo = [
    {'colName': 'CANTIDAD TOTAL ', 'col': 'A', 'sqlName': 'CANTIDAD TOTAL ', 'tipo': 'default'},
    {'colName': 'SEMANA', 'col': 'B', 'sqlName': 'SEMANA', 'tipo': 'default'},
    {'colName': 'N° DE INFORME', 'col': 'C', 'sqlName': 'N° DE INFORME', 'tipo': 'default'},
    {'colName': 'CODIGO DEL ASESOR', 'col': 'D', 'sqlName': 'CODIGO DEL ASESOR', 'tipo': 'default'},
    {'colName': 'NOMBRE DEL ASESOR', 'col': 'E', 'sqlName': 'NOMBRE DEL ASESOR', 'tipo': 'default'},
    {'colName': 'CONEXIÓN ', 'col': 'F', 'sqlName': 'CONEXIÓN ', 'tipo': 'default'},
    {'colName': 'ANTIGÜEDAD AGENTE', 'col': 'G', 'sqlName': 'ANTIGÜEDAD AGENTE', 'tipo': 'default'},
    {'colName': 'CAMPAÑA', 'col': 'H', 'sqlName': 'CAMPAÑA', 'tipo': 'default'},
    {'colName': 'PROVEEDOR', 'col': 'I', 'sqlName': 'PROVEEDOR', 'tipo': 'default'},
    {'colName': 'FECHA DE MONITOREO', 'col': 'J', 'sqlName': 'FECHA DE MONITOREO', 'tipo': 'default'},
    {'colName': 'SN - IPCC', 'col': 'K', 'sqlName': 'SN - IPCC', 'tipo': 'no_duplicado'},
    {'colName': 'FECHA DE LA LLAMADA', 'col': 'L', 'sqlName': 'FECHA DE LA LLAMADA', 'tipo': 'default'},
    {'colName': 'HORA DE LA LLAMADA', 'col': 'M', 'sqlName': 'HORA DE LA LLAMADA', 'tipo': 'default'},
    {'colName': 'TMG', 'col': 'N', 'sqlName': 'TMG', 'tipo': 'default'},
    {'colName': 'TMG MONITOREO', 'col': 'O', 'sqlName': 'TMG MONITOREO', 'tipo': 'default'},
    {'colName': 'NOMBRE DEL CLIENTE', 'col': 'P', 'sqlName': 'NOMBRE DEL CLIENTE', 'tipo': 'default'},
    {'colName': 'N° TELF DEL QUE LLLAMA (MSISDN)', 'col': 'Q', 'sqlName': 'N° TELF DEL QUE LLLAMA MSISDN', 'tipo': 'str'},
    {'colName': ' NÚMERO IDENTIFICADO (TELEFONO EN CONSULTA)', 'col': 'R', 'sqlName': 'NUMERO IDENTIFICADO TELEFONO EN CONSULTA', 'tipo': 'str'},
    {'colName': 'TIPO DE LLAMADA', 'col': 'S', 'sqlName': 'TIPO DE LLAMADA', 'tipo': 'default'},
    {'colName': 'TIPO DE SERVICIO', 'col': 'T', 'sqlName': 'SERVICIO', 'tipo': 'default'},
    {'colName': 'MOTIVO DE LLAMADA', 'col': 'U', 'sqlName': 'MOTIVO DE LLAMADA', 'tipo': 'default'},
    {'colName': 'SUBMOTIVO DE LLAMADA', 'col': 'V', 'sqlName': 'SUBMOTIVO DE LLAMADA', 'tipo': 'default'},
    {'colName': 'MOTIVO DE LLAMADA 2', 'col': 'W', 'sqlName': 'MOTIVO DE LLAMADA 2', 'tipo': 'default'},
    {'colName': 'SUBMOTIVO DE LLAMADA 2', 'col': 'X', 'sqlName': 'SUBMOTIVO DE LLAMADA 2', 'tipo': 'default'},
    {'colName': 'DESCRIPCIÓN DE LA LLAMADA', 'col': 'Y', 'sqlName': 'DESCRIPCIÓN DE LA LLAMADA', 'tipo': 'default'},
    {'colName': 'TIPIFICAICON  AGENTE SIAC', 'col': 'Z', 'sqlName': 'TIPIFICAICON AGENTE SIAC', 'tipo': 'default'},
    {'colName': 'SERVICIO AFECTADO', 'col': 'AA', 'sqlName': 'SERVICIO AFECTADO', 'tipo': 'default'},
    {'colName': 'DETALLE DEL INCONVENIENTE', 'col': 'AB', 'sqlName': 'DETALLE DEL INCONVENIENTE', 'tipo': 'default'},
    {'colName': 'LA LLAMADA ES REINCIDENCIA', 'col': 'AC', 'sqlName': 'LA LLAMADA ES REINCIDENCIA', 'tipo': 'default'},
    {'colName': 'INDICÓ EL NOMBRE DEL CLIENTE EN EL SALUDO', 'col': 'AD', 'sqlName': 'INDICO EL NOMBRE DEL CLIENTE EN EL SALUDO', 'tipo': 'default'},
    {'colName': 'PIDIÓ EL NÚMERO EN CONSULTA (MÓVIL) O DOCUMENTO DE IDENTIDAD (FIJA) PARA IDENTIFICAR EL SERVICIO', 'col': 'AE', 'sqlName': 'PIDIO EL NÚMERO EN CONSULTA O DOCUMENTO DE IDENTIDAD', 'tipo': 'default'},
    {'colName': 'ALERTA POSIBLE MALA DICCIÓN', 'col': 'AF', 'sqlName': 'ALERTA POSIBLE MALA DICCION', 'tipo': 'default'},
    {'colName': 'ALERTA DE POSIBLE INDOLENCIA EN LA ATENCIÓN', 'col': 'AG', 'sqlName': 'ALERTA DE POSIBLE INDOLENCIA EN LA ATENCION', 'tipo': 'default'},
    {'colName': 'ASESOR CONTABA CON PROCESO ADECUADO PARA ATENCIÓN', 'col': 'AH', 'sqlName': 'ASESOR CONTABA CON PROCESO ADECUADO PARA ATENCION', 'tipo': 'default'},
    {'colName': 'NOMBRE DEL MONITOREADOR O RESPONSABLE DEL MONITOREO', 'col': 'AI', 'sqlName': 'NOMBRE DEL MONITOREADOR O RESPONSABLE DEL MONITOREO', 'tipo': 'default'},
    {'colName': '1.1 Saluda conforme a lo indicado en el Lineamiento de Atención ', 'col': 'AJ', 'sqlName': '1#1 Saluda conforme a lo indicado en el Lineamiento de Atención', 'tipo': 'default'},
    {'colName': '1.1.1 Inmediatamente ingresa la llamada', 'col': 'AK', 'sqlName': '1#1#1 Inmediatamente ingresa la llamada', 'tipo': 'default'},
    {'colName': '1.1.2 Aplica saludo de bienvenida', 'col': 'AL', 'sqlName': '1#1#2 Aplica saludo de bienvenida', 'tipo': 'default'},
    {'colName': '1.1.3 Presentación del AS con nombre y apellido', 'col': 'AM', 'sqlName': '1#1#3 Presentación del AS con nombre y apellido', 'tipo': 'default'},
    {'colName': '1.1.4 Menciona el nombre del cliente', 'col': 'AN', 'sqlName': '1#1#4 Menciona el nombre del cliente', 'tipo': 'default'},
    {'colName': '1.1.5 Menciona el número de la línea', 'col': 'AO', 'sqlName': '1#1#5 Menciona el número de la línea', 'tipo': 'default'},
    {'colName': '1.1.6 Motivo del inconveniente', 'col': 'AP', 'sqlName': '1#1#6 Motivo del inconveniente', 'tipo': 'default'},
    {'colName': ' 1. Bienvenida', 'col': 'AQ', 'sqlName': 'PONDERACION_1', 'tipo': 'cf'},
    {'colName': '2.1 Solo si no es clara la necesidad (información, preocupación, problema), reconfirma, realiza una pregunta de precisión y/o aclara sin criticar o corregir negativamente al cliente', 'col': 'AR', 'sqlName': '2#1 Solo si no es clara la necesidad', 'tipo': 'default'},
    {'colName': '2.2 Diagnostica correctamente la necesidad', 'col': 'AS', 'sqlName': '2#2 Diagnostica correctamente la necesidad', 'tipo': 'default'},
    {'colName': '2.3 Evita ser negativo ante la necesidad expuesta', 'col': 'AT', 'sqlName': '2#3 Evita ser negativo ante la necesidad expuesta', 'tipo': 'default'},
    {'colName': '2.3.1 Sin poner en duda lo expuesto por el cliente', 'col': 'AU', 'sqlName': '2#3#1 Sin poner en duda lo expuesto por el cliente', 'tipo': 'default'},
    {'colName': '2.3.2 Sin hacerlo sentir menos por no entender o saber', 'col': 'AV', 'sqlName': '2#3#2 Sin hacerlo sentir menos por no entender o saber', 'tipo': 'default'},
    {'colName': '2.3.3 Sin hacerlo sentir responsable del problema que pudo haber ocasionado en el servicio', 'col': 'AW', 'sqlName': '2#3#3 Sin hacerlo sentir responsable del problema que pudo haber', 'tipo': 'default'},
    {'colName': '2.4 Evita realizar validaciones innecesarias', 'col': 'AX', 'sqlName': '2#4 Evita realizar validaciones innecesarias', 'tipo': 'default'},
    {'colName': '2.4.1 Datos del servicio que figuran en el sistema', 'col': 'AY', 'sqlName': '2#4#1 Datos del servicio que figuran en el sistema', 'tipo': 'default'},
    {'colName': '2.4.2 Datos que ya fueron brindados por el cliente', 'col': 'AZ', 'sqlName': '2#4#2 Datos que ya fueron brindados por el cliente', 'tipo': 'default'},
    {'colName': '2.5 De acuerdo con lo expuesto por el cliente y/o por lo revisado en sistemas, confirma con el cliente que existe alguna atención previa por el mismo motivo.', 'col': 'BA', 'sqlName': '2#5 De acuerdo con lo expuesto por el cliente y_o por lo revisad', 'tipo': 'default'},
    {'colName': ' 2. Diagnóstico de la necesidad', 'col': 'BB', 'sqlName': 'PONDERACION_2', 'tipo': 'cf'},
    {'colName': '3.1 Brinda información completa de acuerdo a la necesidad del cliente, incluido el número de caso/interacción según corresponda. Ante falta de información de proceso, escala con supervisor.', 'col': 'BC', 'sqlName': '3#1 Brinda información completa de acuerdo a la necesidad del cl', 'tipo': 'default'},
    {'colName': 'Motivo de consulta 1 (en caso de mala información, especificar el o los motivos)', 'col': 'BD', 'sqlName': 'Motivo de consulta 1 3#1', 'tipo': 'default'},
    {'colName': 'Motivo de consulta 2(en caso de mala información, especificar el o los motivos)', 'col': 'BE', 'sqlName': 'Motivo de consulta 2 3#1', 'tipo': 'default'},
    {'colName': '3.2 Realiza los descartes y pasos de acuerdo a lo establecido en el procedimiento', 'col': 'BF', 'sqlName': '3#2 Realiza los descartes y pasos de acuerdo a lo establecido en', 'tipo': 'default'},
    {'colName': '3.2.1 Busca solución al inconveniente detectado haciendo uso de la Matriz de descartes AT en el orden lógico establecido.', 'col': 'BG', 'sqlName': '3#2#1 Busca solución al inconveniente detectado', 'tipo': 'default'},
    {'colName': ' Motivo de Consulta 1(en caso de no realizarlo, especificar el o los motivos)', 'col': 'BH', 'sqlName': 'Motivo de Consulta 1 3#2#1', 'tipo': 'default'},
    {'colName': ' Motivo de Consulta 2(en caso de no realizarlo, especificar el o los motivos)', 'col': 'BI', 'sqlName': 'Motivo de Consulta 2 3#2#1', 'tipo': 'default'},
    {'colName': '3.2.2 Realiza todos los descartes para dar solución al cliente evitando la generación del caso.  ', 'col': 'BJ', 'sqlName': '3#2#2 Realiza todos los descartes para dar solución', 'tipo': 'default'},
    {'colName': ' Motivo de Consulta 1(en caso de no realizarlo, especificar el o los motivos)2', 'col': 'BK', 'sqlName': 'Motivo de Consulta 1 3#2#2', 'tipo': 'default'},
    {'colName': ' Motivo de Consulta 2(en caso de no realizarlo, especificar el o los motivos)3', 'col': 'BL', 'sqlName': 'Motivo de Consulta 2 3#2#2', 'tipo': 'default'},
    {'colName': '3.3 Registra la gestión', 'col': 'BM', 'sqlName': '3#3 Registra la gestión', 'tipo': 'default'},
    {'colName': '3.3.1 Tipifica todas las consultas', 'col': 'BN', 'sqlName': '3#3#1 Tipifica todas las consultas', 'tipo': 'default'},
    {'colName': '3.3.2 La tipificación utilizada es la correcta', 'col': 'BO', 'sqlName': '3#3#2 La tipificación utilizada es la correcta', 'tipo': 'default'},
    {'colName': '3.3.3 Las notas y/o plantillas de la tipificación son correctas. ', 'col': 'BP', 'sqlName': '3#3#3 Las notas y_o plantillas de la tipificación son correctas#', 'tipo': 'default'},
    {'colName': ' 3. Solución Efectiva', 'col': 'BQ', 'sqlName': 'PONDERACION_3', 'tipo': 'cf'},
    {'colName': '4.1 Consulta al cliente si entendió la gestión o explicación brindada', 'col': 'BR', 'sqlName': '4#1 Consulta al cliente si entendió la gestión o explicación bri', 'tipo': 'default'},
    {'colName': '4.2 En caso de dudas las clarifica de forma adecuada asegurando el entendimiento del cliente', 'col': 'BS', 'sqlName': '4#2 En caso de dudas las clarifica de forma adecuada asegurando ', 'tipo': 'default'},
    {'colName': '4.3 Si la solución no es en línea, refuerza que se atenderá su necesidad', 'col': 'BT', 'sqlName': '4#3 Si la solución no es en línea refuerza que se atenderá su n', 'tipo': 'default'},
    {'colName': ' 4. Validación de la Solución', 'col': 'BU', 'sqlName': 'PONDERACION_4', 'tipo': 'cf'},
    {'colName': '5.1 Realiza recomendaciones de Valor', 'col': 'BV', 'sqlName': '5#1 Realiza recomendaciones de Valor', 'tipo': 'default'},
    {'colName': ' (Indicar recomendación realizada)', 'col': 'BW', 'sqlName': 'Recomendación realizada 5#1', 'tipo': 'default'},
    {'colName': ' 5. Recomendación', 'col': 'BX', 'sqlName': 'PONDERACION_5', 'tipo': 'cf'},
    {'colName': '6.1 Informa al cliente que buscamos mejorar cada vez más la experiencia que damos a nuestros clientes ', 'col': 'BY', 'sqlName': '6#1 Informa al cliente que buscamos mejorar cada vez más la expe', 'tipo': 'default'},
    {'colName': '6.2 Informa de manera clara al cliente  que será derivado a una encuesta ', 'col': 'BZ', 'sqlName': '6#2 Informa de manera clara al cliente  que será derivado a una ', 'tipo': 'default'},
    {'colName': '6.2.1  Sin mencionar una escala en particular', 'col': 'CA', 'sqlName': '6#2#1 Sin mencionar una escala en particular', 'tipo': 'default'},
    {'colName': '6.3 Agradece al cliente por la espera y demoras generadas en la llamada', 'col': 'CB', 'sqlName': '6#3 Agradece al cliente por la espera y demoras generadas en la ', 'tipo': 'default'},
    {'colName': '6.4 La despedida es de manera natural y fluida', 'col': 'CC', 'sqlName': '6#4 La despedida es de manera natural y fluida', 'tipo': 'default'},
    {'colName': ' 6. Finalizar Experiencia', 'col': 'CD', 'sqlName': 'PONDERACION_6', 'tipo': 'cf'},
    {'colName': '7.1 Se dirige al cliente por su nombre utilizando el “Usted” durante el transcurso de la llamada', 'col': 'CE', 'sqlName': '7#1 Se dirige al cliente por su nombre utilizando el Usted', 'tipo': 'default'},
    {'colName': '7.2 Evita utilizar términos no permitidos en el Lineamiento de Atención', 'col': 'CF', 'sqlName': '7#2 Evita utilizar términos no permitidos en el Lineamiento', 'tipo': 'default'},
    {'colName': '7.2.1 Caballero/joven u otro no solicitado expresamente.', 'col': 'CG', 'sqlName': '7#2#1 Caballero_joven u otro no solicitado expresamente', 'tipo': 'default'},
    {'colName': '7.2.2 Política o religión, excepto si el cliente hace una referencia inicial', 'col': 'CH', 'sqlName': '7#2#2 Política o religión excepto si el cliente hace una refere', 'tipo': 'default'},
    {'colName': '7.3 Se expresa con entusiasmo durante la llamada', 'col': 'CI', 'sqlName': '7#3 Se expresa con entusiasmo durante la llamada', 'tipo': 'default'},
    {'colName': '7.4 Se expresa con naturalidad durante la llamada', 'col': 'CJ', 'sqlName': '7#4 Se expresa con naturalidad durante la llamada', 'tipo': 'default'},
    {'colName': '7.5 Escucha atentamente al cliente ', 'col': 'CK', 'sqlName': '7#5 Escucha atentamente al cliente', 'tipo': 'default'},
    {'colName': '7.5.1 Sin interrumpir abruptamente', 'col': 'CL', 'sqlName': '7#5#1 Sin interrumpir abruptamente', 'tipo': 'default'},
    {'colName': '7.5.2 Sin realizar suposiciones antes que el cliente termine de hablar o explicar', 'col': 'CM', 'sqlName': '7#5#2 Sin realizar suposiciones antes que el cliente termine', 'tipo': 'default'},
    {'colName': '7.6 Según la o las situaciones expuestas por el cliente, empatiza utilizando frases relacionadas a la situación', 'col': 'CN', 'sqlName': '7#6 Segun la o las situaciones expuestas por el cliente empatiz', 'tipo': 'default'},
    {'colName': '7.6.1 De forma natural', 'col': 'CO', 'sqlName': '7#6#1 De forma natural', 'tipo': 'default'},
    {'colName': '7.6.2 Tono de voz transmite emociones', 'col': 'CP', 'sqlName': '7#6#2 Tono de voz transmite emociones', 'tipo': 'default'},
    {'colName': '7.6.3 Transmite interés y preocupación', 'col': 'CQ', 'sqlName': '7#6#3 Transmite interés y preocupación', 'tipo': 'default'},
    {'colName': '7.7 Interactúa con el cliente', 'col': 'CR', 'sqlName': '7#7 Interactúa con el cliente', 'tipo': 'default'},
    {'colName': '7.7.1 Informa al cliente las acciones que está realizando', 'col': 'CS', 'sqlName': '7#7#1 Informa al cliente las acciones que está realizando', 'tipo': 'default'},
    {'colName': '7.7.2 Evita usar locución de espera (hold), salvo necesidad justificada e informada al cliente', 'col': 'CT', 'sqlName': '7#7#2 Evita usar locución de espera hold salvo necesidad', 'tipo': 'default'},
    {'colName': '7.8 Evita realizar comentarios negativos sobre Claro. ', 'col': 'CU', 'sqlName': '7#8 Evita realizar comentarios negativos sobre Claro', 'tipo': 'default'},
    {'colName': ' 7. Actitud en toda la atención', 'col': 'CV', 'sqlName': 'PONDERACION_7', 'tipo': 'cf'},
    {'colName': 'CALIFICACIÓN FINAL', 'col': 'DC', 'sqlName': 'SUB - CALIFICACIÓN', 'tipo': 'cf'},
    {'colName': 'ERRORES CRITICOS DE USUARIO FINAL', 'col': 'CX', 'sqlName': 'ERRORES CRITICOS DE USUARIO FINAL', 'tipo': 'default'},
    {'colName': 'ERRORES CRITICOS DE NEGOCIO', 'col': 'CY', 'sqlName': 'ERRORES CRITICOS DE NEGOCIO', 'tipo': 'default'},
    {'colName': 'ERRORES CRITICOS DE CUMPLIMIENTO', 'col': 'CZ', 'sqlName': 'ERRORES CRITICOS DE CUMPLIMIENTO', 'tipo': 'default'},
    {'colName': 'TOTAL ERRORES CRITICOS', 'col': 'DA', 'sqlName': 'TOTAL ERRORES CRITICOS', 'tipo': 'default'},
    {'colName': 'TOTAL ERRORES NO CRITICOS', 'col': 'DB', 'sqlName': 'TOTAL ERRORES NO CRITICOS', 'tipo': 'default'},
    {'colName': 'CALIFICACIÓN FINAL', 'col': 'DC', 'sqlName': 'CALIFICACIÓN FINAL', 'tipo': 'cf'},
    {'colName': 'AS induce al cliente a cortar la llamada por dejarlo en espera por tiempo prolongado', 'col': 'DD', 'sqlName': 'AS induce al cliente a cortar la llamada por dejarlo en espera p', 'tipo': 'default'},
    {'colName': 'AS transfiere a cualquier locución cuando aún no ha concluido con la atención ', 'col': 'DE', 'sqlName': 'AS transfiere a cualquier locución cuando aún no ha concluido co', 'tipo': 'default'},
    {'colName': 'AS se dirige en la llamada mencionando palabras soeces.', 'col': 'DF', 'sqlName': 'AS se dirige en la llamada mencionando palabras soeces', 'tipo': 'default'},
    {'colName': 'AS se dirige al cliente con mala actitud y/o con sarcasmo.', 'col': 'DG', 'sqlName': 'AS se dirige al cliente con mala actitud y_o con sarcasmo', 'tipo': 'default'},
    {'colName': 'AS conversa con un tercero o hace ruidos molestos (sonidos, golpes, risas, etc.) durante la atención', 'col': 'DH', 'sqlName': 'AS conversa con un tercero o hace ruidos molestos', 'tipo': 'default'},
    {'colName': 'AS no cuenta con una diccion correcta en la atencion ', 'col': 'DI', 'sqlName': 'AS no cuenta con una diccion correcta en la atencion', 'tipo': 'default'},
    {'colName': 'AS deriva a otro canal cuando la atencion no lo amerita', 'col': 'DJ', 'sqlName': 'AS deriva a otro canal cuando la atencion no lo amerita', 'tipo': 'default'},
    {'colName': 'COMENTARIO  MALA PRÁCTICA', 'col': 'DK', 'sqlName': 'COMENTARIO MALA PRÁCTICA', 'tipo': 'default'},
    {'colName': 'FCR', 'col': 'DL', 'sqlName': 'FCR', 'tipo': 'default'},
    {'colName': 'RESPONSABILIDAD DE NO FCR', 'col': 'DM', 'sqlName': 'RESPONSABILIDAD DE NO FCR', 'tipo': 'default'},
    {'colName': 'MOTIVO DE NO FCR', 'col': 'DN', 'sqlName': 'MOTIVO DE NO FCR', 'tipo': 'default'},
    {'colName': 'PROCESO CLARO NO FCR', 'col': 'DO', 'sqlName': 'PROCESO CLARO NO FCR', 'tipo': 'default'},
    {'colName': 'DETALLE DE NO FCR', 'col': 'DP', 'sqlName': 'DETALLE DE NO FCR', 'tipo': 'default'},
    {'colName': 'ACCION QUE REALIZA EL ASESOR', 'col': 'DQ', 'sqlName': 'ACCION QUE REALIZA EL ASESOR', 'tipo': 'default'},
    {'colName': 'TIENE ALARMA', 'col': 'DR', 'sqlName': 'TIENE ALARMA', 'tipo': 'default'},
    {'colName': 'OBSERVACION / RECOMENDACIÓN', 'col': 'DS', 'sqlName': 'OBSERVACION_RECOMENDACION', 'tipo': 'default'},
    {'colName': 'LLAMADA ES CON AUDIO O VIDEO ', 'col': 'DT', 'sqlName': 'LLAMADA ES CON AUDIO O VIDEO', 'tipo': 'default'},
]