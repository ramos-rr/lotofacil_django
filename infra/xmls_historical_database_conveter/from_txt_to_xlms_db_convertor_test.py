from decouple import config
from .from_txt_to_xlms_db_convertor import XlmsConverter


def test_export_to_xlms_from_txt():
    txt_file_path = "C:/Users/rafae/PycharmProjects/lotofacil_django/infra/database/test/hist_concursos_89.txt"
    xlms_folder_path = config('XLMS_FOLDER_PATH_TEST')
    validator = XlmsConverter().export_to_xlms_from_txt(txt_file_path=txt_file_path, xlsx_folder_path=xlms_folder_path)
    assert validator.conta_linha == validator.last_game
    assert validator.xlms_file_path == f'{xlms_folder_path}lotofacil_hist_concursos_{validator.last_game}.xlsx'
