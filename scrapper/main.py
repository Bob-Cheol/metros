from extractors.extractor_for_game_info import extract_game_infos
from extractors.extractor_for_player_info import extract_player_infos
from extractors.extractor_for_player_record import extract_player_records
from extractors.extractor_for_game_boxscore import extract_game_boxscores
from helper.database_helper import upload_game_info_to_database, upload_player_info_to_database, upload_batter_by_season_to_database, upload_batter_by_game_to_database, upload_pitcher_by_season_to_database, upload_pitcher_by_game_to_database

if __name__ == '__main__':
  team_id = '17818'
  start_year = 2016
  end_year = 2022

  # upload game_info
  if True:
    for season in range(start_year, end_year+1):
      print('uploading game_infos in season :', season)
      game_infos = extract_game_infos(team_id, season)
      upload_game_info_to_database(game_infos, season)

  # upload player_info
  if True:
    print('uploading player_infos')
    player_infos = extract_player_infos(team_id)
    upload_player_info_to_database(player_infos)

  # upload player records : batter_by_season, batter_by_games, pitcher_by_season, pitcher_by_games
  if True:
    player_infos = extract_player_infos(team_id)
    for player_info in player_infos:
      player_name = player_info['player_name']
      player_id = player_info['player_id']
      print(f'uploading player {player_name}')
      for season in range(start_year, end_year+1):
        print(f'{season}..', end='')
        batter_by_games, batter_by_season, pitcher_by_games, pitcher_by_season = extract_player_records(team_id, season, player_id)
        if batter_by_season['t_game'] > 0:
          upload_batter_by_game_to_database(batter_by_games, player_id, player_name, team_id, season)
          upload_batter_by_season_to_database(batter_by_season, player_id, player_name, team_id, season)
        if pitcher_by_season['t_game'] > 0:
          upload_pitcher_by_game_to_database(pitcher_by_games, player_id, player_name, team_id, season)
          upload_pitcher_by_season_to_database(pitcher_by_season, player_id, player_name, team_id, season)
      print('')

  # extract_boxscores('17818', '1472948')
