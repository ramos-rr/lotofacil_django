from collections import namedtuple


class OldGamesGetter:
    """
    Class to Get Old games from a HTML file saved locally
    Atention: It does run ONLINE, just for an already saved HTML page
    """
    raw_games_list = []

    def __init__(self):
        self.get_old_games_result = namedtuple(typename='GET_Old_Games',
                                               field_names="line_check, last_game, txt_file_path")

    def get_old_games(self, html_file_path, txt_folder_path) -> 'GET_Old_Games':
        """
        Method to get html lines, treat, and create TXT file with all passed games
        :param html_file_path: HTML file path
        :param txt_folder_path: place to save TXT file
        :return: None
        """
        # Open the HTML file and treat line by line to get only the important data
        try:
            with open(html_file_path, mode='rt', encoding='utf8') as page:
                line_check = 0
                for line in page:
                    if '<td>' in line[:4] and '<table>' in line[-8:]:
                        line = line.replace('<td>', '').replace('</td>', ',').replace('<table>', '')
                        virg = line.rfind(',')
                        self.raw_games_list.append(f'{line[:virg]}\n')
                        line_check += 1
                virg = self.raw_games_list[-1].find(',')
                last_game = self.raw_games_list[-1][:virg]
                txt_file_path = f'{txt_folder_path}hist_concursos_{last_game}.txt'

                # Save in TXT
                with open(txt_file_path, 'w') as arquivo:
                    for linha in self.raw_games_list:
                        arquivo.writelines(f'{linha}')

                return self.get_old_games_result(
                    line_check=line_check,
                    last_game=int(last_game),
                    txt_file_path=txt_file_path
                )
        except FileNotFoundError:
            raise FileNotFoundError
