import pytest
from infra.old_games_getter_from_local_html.test import OldGamesGetterSpy
from decouple import config


def test_obtain_old_games():
    html_file_path = config('HTML_FILE_PATH_TEST')
    txt_folder_path = config('TXT_FOLDER_PATH_TEST')
    jogos = OldGamesGetterSpy()
    validation = jogos.get_old_games(html_file_path=html_file_path, txt_folder_path=txt_folder_path)
    assert validation.last_game == validation.line_check
    assert validation.txt_file_path == f"{txt_folder_path}hist_concursos_{validation.last_game}.txt"


def test_obtain_old_games_file_not_found_error():
    html_file_path = ''
    txt_folder_path = ''
    with pytest.raises(FileNotFoundError):
        jogos = OldGamesGetterSpy()
        jogos.get_old_games(html_file_path, txt_folder_path)
