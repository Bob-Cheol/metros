from requests import get
from bs4 import BeautifulSoup

def extract_player_infos(team_id):
  # active players
  response = get(
    f'http://www.gameone.kr/club/info/player?club_idx={team_id}'
  )

  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    infos = soup.find_all('dl', class_='info')

    player_infos = []
    for info in infos:
      group_code = info.find_all('input')[1]['value']
      player_no, player_name = info.find('dt').text.split('.')
      main_position, hand_type = info.find('dd').text.split('|')
      main_position = main_position.replace(' ','')
      hand_type = hand_type.replace(' ','')
      player_info = {
        'player_id':group_code,
        'player_name':player_name,
        'player_no':player_no,
        'status':'active',
        'main_position':main_position if main_position != '미지정' else None,
        'hand_type':hand_type if hand_type != '' else None,
        'team_id':team_id
      }
      player_infos.append(player_info)

  # inactive players
  response = get(
    f'http://www.gameone.kr/club/info/player?club_idx={team_id}&pos=R'
  )

  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    infos = soup.find_all('dl', class_='info')

    for info in infos:
      group_code = info.find_all('input')[1]['value']
      player_no, player_name = info.find('dt').text.split('.')
      main_position, hand_type = info.find('dd').text.split('|')
      main_position = main_position.replace(' ','')
      hand_type = hand_type.replace(' ','')
      player_info = {
        'player_id':group_code,
        'player_name':player_name,
        'player_no':player_no,
        'status':'inactive',
        'main_position':main_position if main_position != '미지정' else None,
        'hand_type':hand_type if hand_type != '' else None,
        'team_id':team_id
      }
      player_infos.append(player_info)

    return player_infos
  else:
    print('Response Error : status_code', response.status_code)
    return None
