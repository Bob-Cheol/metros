from requests import get
from bs4 import BeautifulSoup

def extract_player_records(team_id, season, player_id):
  response = get(
    f'http://www.gameone.kr/club/info/ranking/table/?season={season}&club_idx={team_id}&group_code={player_id}&game_type=0'
  )

  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    batter_table, pitcher_table = soup.find_all('table', class_='ranking_table')

    # batter_by_games
    batter_season, batter_columns = batter_table.find('thead').find_all('tr')
    batter_column_names = [
      cn['sort']
      for cn
      in batter_columns.find_all('th', class_='sort')
    ]
    game_records = batter_table.find('tbody').find_all('tr')

    batter_by_games = []
    for game_record in game_records:
      batter_by_game = {}
      batter_by_game['date'] = game_record.find('th', class_='fixed').text
      for colname, record in zip(batter_column_names, game_record.find_all('td')):
        if record.text != '-':
          batter_by_game[colname] = record.text
      batter_by_games.append(batter_by_game)

    # batter_by_season
    batter_season_records = batter_season.find_all('th')
    batter_season_records.pop(0)
    batter_season_records = [
      record.text
      for record
      in batter_season_records
    ]
    batter_by_season = {
      't_game':len(batter_by_games)
    }
    for colname, record in zip(batter_column_names, batter_season_records):
      if record != '-':
        batter_by_season[colname] = record

    # pitcher_by_games
    pitcher_season, pitcher_columns = pitcher_table.find('thead').find_all('tr')
    pitcher_column_names = [
      cn['sort']
      for cn
      in pitcher_columns.find_all('th', class_='sort')
    ]
    game_records = pitcher_table.find('tbody').find_all('tr')

    pitcher_by_games = []
    for game_record in game_records:
      pitcher_by_game = {}
      pitcher_by_game['date'] = game_record.find('th', class_='fixed').text
      for colname, record in zip(pitcher_column_names, game_record.find_all('td')):
        if record.text != '-':
          pitcher_by_game[colname] = record.text

      inn_sum = 0
      for inn_part in pitcher_by_game['inn'].split(' '):
        inn_part = 1/3 if inn_part == '⅓' else 2/3 if inn_part == '⅔' else inn_part
        inn_sum += float(inn_part)
      pitcher_by_game['inn'] = inn_sum

      pitcher_by_games.append(pitcher_by_game)


    # pitcher_by_season
    pitcher_season_records = pitcher_season.find_all('th')
    pitcher_season_records.pop(0)
    pitcher_season_records = [
      record.text
      for record
      in pitcher_season_records
    ]
    pitcher_by_season = {
      't_game':len(pitcher_by_games)
    }
    for colname, record in zip(pitcher_column_names, pitcher_season_records):
      if record != '-':
        pitcher_by_season[colname] = record

    inn_sum = 0
    for inn_part in pitcher_by_season['inn'].split(' '):
      inn_part = 1/3 if inn_part == '⅓' else 2/3 if inn_part == '⅔' else inn_part
      inn_sum += float(inn_part)
    pitcher_by_season['inn'] = inn_sum

    return batter_by_games, batter_by_season, pitcher_by_games, pitcher_by_season
  else:
    print('Response Error : status_code', response.status_code)
    return None
