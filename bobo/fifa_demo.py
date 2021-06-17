from requests import get as http_get_request

from re import findall


URL = r'https://www.futbin.com/squad-building-challenges/ALL/2807/Festival%20of%20FUTball%20Challenge'

TABLE = '<table class="table table-striped table-black chal_table">'
TEAM_URL_BASE = 'https://www.futbin.com'


PLAYER_PROFILE_REGEX = '<div class="cardetails" style="z-index: 0;" >([\s\S]+?)<div class="player-hover-box" style="display: none;">'


class Player:
    """

    """
    def __init__(self):
        """

        """
        self.name = ''
        self.pc_price = 0
        self.ps_price = 0
        self.xbox_price = 0

    def __str__(self):
        """

        :return:
        """
        _str = ''
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                _str += f'{key}: {value}\n'

        return _str


def get_players():
    """get_players

    :return:
    """
    response = http_get_request(URL)
    content = response.text

    regex = r'<tr>([\s\S]+?)<\/tr>'
    rows = findall(regex, content)

    links = []

    for row in rows:
        if 'td style="padding: 0;"> <img id="squad_mvp_pic"' not in row:
            continue
        link = row[row.find('href="') + len('href="'):]
        link = link[:link.find('">')]
        link = f'{TEAM_URL_BASE}{link}'
        links.append(link)

    index = 0
    for link in links:

        print(f'Parsing link: {link}...')

        response = http_get_request(link)
        content = response.text

        players_profiles = findall(PLAYER_PROFILE_REGEX, content)

        for player_profile in players_profiles:

            player = Player()
            name = player_profile[player_profile.find('data-player-commom="') + len('data-player-commom="'):]
            name = name[:name.find('"')]
            player.name = name

            ps_price = player_profile[player_profile.find('<i class="icon-playstation"></i>') +
                                      len('<i class="icon-playstation"></i>'):]
            ps_price = ps_price[:ps_price.find('</div>')]
            ps_price = ps_price.strip()
            
            player.ps_price = ps_price

            pc_price = player_profile[player_profile.find('<i class="icon-windows8"></i>') +
                                      len('<i class="icon-windows8"></i>'):]
            pc_price = pc_price[:pc_price.find('</div>')]
            pc_price = pc_price.strip()
            player.pc_price = pc_price

            xbox_price = player_profile[player_profile.find('<i class="icon-xbox"></i>') +
                                        len('<i class="icon-xbox"></i>'):]
            xbox_price = xbox_price[:xbox_price.find('</div>')]
            xbox_price = xbox_price.strip()
            player.xbox_price = xbox_price

            file_handler = open(r'D:\players.ipx', 'a')
            index += 1
            file_handler.write(f'\n\n{index}.\n')
            file_handler.write('*' * 80)
            file_handler.write('\n')
            file_handler.write(player.__str__())
            file_handler.write('*' * 80)
            file_handler.write('\n')
            file_handler.close()


if __name__ == '__main__':
    get_players()
