from collections import namedtuple
from typing import Type
from infra.old_games_getter_from_local_html.old_games_getter_from_local_html import OldGamesGetter


class OldGamesGetterSpy:
    """
    Class to Spy the get old games from an HTML file saved locally
    """
    raw_games_list = []

    def __init__(self):
        self.get_old_games_result = namedtuple(typename='GET_Old_Games',
                                               field_names="line_check, last_game, txt_file_path")

    def get_old_games(self, html_file_path, txt_folder_path) -> 'GET_Old_Games':
        """
        Spy funtion to generate tests files
        :param html_file_path: path to the HTML mocked
        :param txt_folder_path: path to the folder for txt file be created
        :return: attributes values
        """
        original_class = OldGamesGetter()
        test = original_class.get_old_games(html_file_path=html_file_path, txt_folder_path=txt_folder_path)

        return self.get_old_games_result(
            line_check=test.line_check,
            last_game=test.last_game,
            txt_file_path=test.txt_file_path
        )
