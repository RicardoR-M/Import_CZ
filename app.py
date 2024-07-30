from configparser import ConfigParser
from fnmatch import fnmatch
from pathlib import Path

from config.adm import adm, adm_db, adm_db_table, adm_xl_firstDataRow, adm_xl_colNameRow, adm_maxColNumber, adm_xl_hoja, adm_xl_colCheckFlag
from config.at_izo import at_izo, at_izo_db, at_izo_db_table, at_izo_xl_firstDataRow, at_izo_xl_colNameRow, at_izo_maxColNumber, at_izo_xl_hoja, at_izo_xl_colCheckFlag
from config.feedback import fb, fb_db, fb_db_table, fb_xl_firstDataRow, fb_xl_colNameRow, fb_maxColNumber, fb_xl_hoja, fb_xl_colCheckFlag
from config.post import post, post_db, post_db_table, post_xl_firstDataRow, post_xl_colNameRow, post_maxColNumber, post_xl_hoja, post_xl_colCheckFlag
from config.tec import tec, tec_db, tec_db_table, tec_xl_firstDataRow, tec_xl_colNameRow, tec_maxColNumber, tec_xl_hoja, tec_xl_colCheckFlag
from config.web_adm import webadm, webadm_db, webadm_db_table, webadm_xl_firstDataRow, webadm_xl_colNameRow, webadm_maxColNumber, webadm_xl_hoja, webadm_xl_colCheckFlag
from config.web_tec import webtec, webtec_db, webtec_db_table, webtec_xl_firstDataRow, webtec_xl_colNameRow, webtec_maxColNumber, webtec_xl_hoja, webtec_xl_colCheckFlag
from config.web_post import webpost, webpost_db, webpost_db_table, webpost_xl_firstDataRow, webpost_xl_colNameRow, webpost_maxColNumber, webpost_xl_hoja, webpost_xl_colCheckFlag
from config.web_at import webat, webat_db, webat_db_table, webat_xl_firstDataRow, webat_xl_colNameRow, webat_maxColNumber, webat_xl_hoja, webat_xl_colCheckFlag
from config.web_bo_ajustes import webboajustes, webboajustes_db, webboajustes_db_table, webboajustes_xl_firstDataRow, webboajustes_xl_colNameRow, webboajustes_maxColNumber, webboajustes_xl_hoja, webboajustes_xl_colCheckFlag
from config.web_bo_analisis import webboanalisis, webboanalisis_db, webboanalisis_db_table, webboanalisis_xl_firstDataRow, webboanalisis_xl_colNameRow, webboanalisis_maxColNumber, webboanalisis_xl_hoja, webboanalisis_xl_colCheckFlag
from config.web_bo_derivacion import webboderivacion, webboderivacion_db, webboderivacion_db_table, webboderivacion_xl_firstDataRow, webboderivacion_xl_colNameRow, webboderivacion_maxColNumber, webboderivacion_xl_hoja, webboderivacion_xl_colCheckFlag
from config.web_bo_reclamos import webboreclamos, webboreclamos_db, webboreclamos_db_table, webboreclamos_xl_firstDataRow, webboreclamos_xl_colNameRow, webboreclamos_maxColNumber, webboreclamos_xl_hoja, webboreclamos_xl_colCheckFlag
from config.web_bo_seguimiento import webboseguimiento, webboseguimiento_db, webboseguimiento_db_table, webboseguimiento_xl_firstDataRow, webboseguimiento_xl_colNameRow, webboseguimiento_maxColNumber, webboseguimiento_xl_hoja, webboseguimiento_xl_colCheckFlag
from config.web_bo_atc import webboatc, webboatc_db, webboatc_db_table, webboatc_xl_firstDataRow, webboatc_xl_colNameRow, webboatc_maxColNumber, webboatc_xl_hoja, webboatc_xl_colCheckFlag
from importa import importa_informe

if __name__ == '__main__':
    # Importa config file
    config = ConfigParser()
    config.read('config.ini')
    path = Path(str(config['config']['bases_folder_path']).replace('\\', '/'))
    q = 0

    for file in path.iterdir():
        if file.is_file() and fnmatch(file.name, '*informe* at *.xlsm'):
            print(f'AT: {file.absolute()}')
            importa_informe(file.absolute(), at_izo, at_izo_db, at_izo_db_table, at_izo_xl_firstDataRow, at_izo_xl_colNameRow, at_izo_maxColNumber, at_izo_xl_hoja, at_izo_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, '*informe*t?cnico*.xlsm'):
            print(f'TEC: {file.absolute()}')
            importa_informe(file.absolute(), tec, tec_db, tec_db_table, tec_xl_firstDataRow, tec_xl_colNameRow, tec_maxColNumber, tec_xl_hoja, tec_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, '*informe*admin*.xlsm'):
            print(f'ADM: {file.absolute()}')
            importa_informe(file.absolute(), adm, adm_db, adm_db_table, adm_xl_firstDataRow, adm_xl_colNameRow, adm_maxColNumber, adm_xl_hoja, adm_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, '*informe*post*.xlsm'):
            print(f'POST: {file.absolute()}')
            importa_informe(file.absolute(), post, post_db, post_db_table, post_xl_firstDataRow, post_xl_colNameRow, post_maxColNumber, post_xl_hoja, post_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, 'feedback.xlsx'):
            print(f'FEEDBACK: {file.absolute()}')
            importa_informe(file.absolute(), fb, fb_db, fb_db_table, fb_xl_firstDataRow, fb_xl_colNameRow, fb_maxColNumber, fb_xl_hoja, fb_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, 'APP MONITOREO_HFC ADMINISTRATIVO_*.xls'):
            print(f'WEB_ADM: {file.absolute()}')
            importa_informe(file.absolute(), webadm, webadm_db, webadm_db_table, webadm_xl_firstDataRow, webadm_xl_colNameRow, webadm_maxColNumber, webadm_xl_hoja, webadm_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, 'APP MONITOREO_HFC TÉCNICO_*.xls'):
            print(f'WEB_TEC: {file.absolute()}')
            importa_informe(file.absolute(), webtec, webtec_db, webtec_db_table, webtec_xl_firstDataRow, webtec_xl_colNameRow, webtec_maxColNumber, webtec_xl_hoja, webtec_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, 'APP MONITOREO_POSTPAGO_*.xls'):
            print(f'WEB_POST: {file.absolute()}')
            importa_informe(file.absolute(), webpost, webpost_db, webpost_db_table, webpost_xl_firstDataRow, webpost_xl_colNameRow, webpost_maxColNumber, webpost_xl_hoja, webpost_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, 'APP MONITOREO_ATENCIÓN TECNOLÓGICA_*.xls'):
            print(f'WEB_AT: {file.absolute()}')
            importa_informe(file.absolute(), webat, webat_db, webat_db_table, webat_xl_firstDataRow, webat_xl_colNameRow, webat_maxColNumber, webat_xl_hoja, webat_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, 'APP MONITOREO_BO AJUSTES_*.xls'):
            print(f'WEB_BO_AJUSTES: {file.absolute()}')
            importa_informe(file.absolute(), webboajustes, webboajustes_db, webboajustes_db_table, webboajustes_xl_firstDataRow, webboajustes_xl_colNameRow, webboajustes_maxColNumber, webboajustes_xl_hoja, webboajustes_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, 'APP MONITOREO_BO ANALISIS_*.xls'):
            print(f'WEB_BO_ANALISIS: {file.absolute()}')
            importa_informe(file.absolute(), webboanalisis, webboanalisis_db, webboanalisis_db_table, webboanalisis_xl_firstDataRow, webboanalisis_xl_colNameRow, webboanalisis_maxColNumber, webboanalisis_xl_hoja, webboanalisis_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, 'APP MONITOREO_BO DERIVACION_*.xls'):
            print(f'WEB_BO_DERIVACION: {file.absolute()}')
            importa_informe(file.absolute(), webboderivacion, webboderivacion_db, webboderivacion_db_table, webboderivacion_xl_firstDataRow, webboderivacion_xl_colNameRow, webboderivacion_maxColNumber, webboderivacion_xl_hoja, webboderivacion_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, 'APP MONITOREO_BO RECLAMOS_*.xls'):
            print(f'WEB_BO_RECLAMOS: {file.absolute()}')
            importa_informe(file.absolute(), webboreclamos, webboreclamos_db, webboreclamos_db_table, webboreclamos_xl_firstDataRow, webboreclamos_xl_colNameRow, webboreclamos_maxColNumber, webboreclamos_xl_hoja, webboreclamos_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, 'APP MONITOREO_BO SEGUIMIENTO_*.xls'):
            print(f'WEB_BO_SEGUIMIENTO: {file.absolute()}')
            importa_informe(file.absolute(), webboseguimiento, webboseguimiento_db, webboseguimiento_db_table, webboseguimiento_xl_firstDataRow, webboseguimiento_xl_colNameRow, webboseguimiento_maxColNumber, webboseguimiento_xl_hoja, webboseguimiento_xl_colCheckFlag)
            q += 1
        if file.is_file() and fnmatch(file.name, 'BACKOFFICE_BO FALLAS ATC_*.xls'):
            print(f'WEB_BO_ATC: {file.absolute()}')
            importa_informe(file.absolute(), webboatc, webboatc_db, webboatc_db_table, webboatc_xl_firstDataRow, webboatc_xl_colNameRow, webboatc_maxColNumber, webboatc_xl_hoja, webboatc_xl_colCheckFlag)
            q += 1

    print(f'Cantidad de informes importados: {q}')
