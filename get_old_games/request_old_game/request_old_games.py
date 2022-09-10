import requests


class OldGamesGetter:
    def __init__(self):
        self.raw_games_list = []

    def obtain_olg_games(self):
        with open("C:/Users/rafae/PycharmProjects/lotofacil_django/get_old_games/resultados_lotofacil_CAIXA.html",
                  mode='rt',
                  encoding='utf8') as page:
            for line in page:
                self.validate_line()
                self.raw_games_list.append(line)


if __name__ == '__main__':
    jogos = OldGamesGetter()
    jogos.obtain_olg_games()
