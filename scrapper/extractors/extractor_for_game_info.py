from requests import get
from bs4 import BeautifulSoup

def extract_game_infos(team_id, season, page=1, game_type=0, lig_idx=0, group=0, month=0):
  response = get(
    f'http://www.gameone.kr/club/info/schedule/result?club_idx={team_id}&season={season}&page={page}&game_type={game_type}&lig_idx={lig_idx}&group={group}&month={month}'
  )

  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    game_table = soup.find('table', class_='game_table')
    table_body = game_table.find_all('tr')
    table_body.pop(0)

    game_infos = []
    for row in table_body:
      values = row.find_all('td')
      date_time = values.pop(0).text
      league = values.pop(0).text
      stadium = values.pop(0).text
      game = values.pop(0)
      team_score = game.find_all('div')
      vs_team_idx = None if team_score[0].find('a') is None else team_score[0].find('a')['href'].split('club_idx=')[1]
      exp_win = team_score[0].find('span', class_='exp_win')
      home_team_name = team_score[1].find('span', class_='team_name').text
      home_score = team_score[1].find('span', class_='score').text
      away_team_name = team_score[2].find('span', class_='team_name').text
      away_score = team_score[2].find('span', class_='score').text
      boxscore_url = values.pop(0)
      game_idx = boxscore_url.find('a')['href'].split('game_idx=')[1]
      game_info = {
        'game_id':game_idx,
        'date_time':date_time,
        'league':league,
        'stadium':stadium,
        'home_team_id':team_id if home_team_name == 'Metros' else vs_team_idx,
        'home_team_name':home_team_name,
        'home_score':home_score,
        'away_team_id':team_id if away_team_name == 'Metros' else vs_team_idx,
        'away_team_name':away_team_name,
        'away_score':away_score,
        'exp_win':None if exp_win is None else exp_win.text
      }
      game_infos.append(game_info)

    if int(soup.find('a', class_='next')['href'].split('page=')[1]) > page:
      while True:
        page += 1
        response = get(
          f'http://www.gameone.kr/club/info/schedule/result?club_idx={team_id}&season={season}&page={page}&game_type={game_type}&lig_idx={lig_idx}&group={group}&month={month}'
        )
        soup = BeautifulSoup(response.text, 'html.parser')
        game_table = soup.find('table', class_='game_table')
        table_body = game_table.find_all('tr')
        table_body.pop(0)

        for row in table_body:
          values = row.find_all('td')
          date_time = values.pop(0).text
          league = values.pop(0).text
          stadium = values.pop(0).text
          game = values.pop(0)
          team_score = game.find_all('div')
          vs_team_idx = None if team_score[0].find('a') is None else team_score[0].find('a')['href'].split('club_idx=')[1]
          exp_win = team_score[0].find('span', class_='exp_win')
          home_team_name = team_score[1].find('span', class_='team_name').text
          home_score = team_score[1].find('span', class_='score').text
          away_team_name = team_score[2].find('span', class_='team_name').text
          away_score = team_score[2].find('span', class_='score').text
          boxscore_url = values.pop(0)
          game_idx = boxscore_url.find('a')['href'].split('game_idx=')[1]
          game_info = {
            'game_id':game_idx,
            'date_time':date_time,
            'league':league,
            'stadium':stadium,
            'home_team_id':team_id if home_team_name == 'Metros' else vs_team_idx,
            'home_team_name':home_team_name,
            'home_score':home_score,
            'away_team_id':team_id if away_team_name == 'Metros' else vs_team_idx,
            'away_team_name':away_team_name,
            'away_score':away_score,
            'exp_win':None if exp_win is None else exp_win.text
          }
          game_infos.append(game_info)

        if int(soup.find('a', class_='next')['href'].split('page=')[1]) == page:
          break

    return game_infos
  else:
    print('Response Error : status_code', response.status_code)
    return None
