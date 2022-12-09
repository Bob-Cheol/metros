import os
import psycopg2

def get_connection_cursor():
  # connect to DB
  conn = psycopg2.connect(
    host=os.environ['METROS_DB_HOST'],
    dbname=os.environ['METROS_DB_NAME'],
    port=5432,
    user=os.environ['METROS_DB_USER'],
    password=os.environ['METROS_DB_PW'],
    options='-c search_path=source'
  )
  conn.set_session(autocommit=True)
  cur = conn.cursor()

  return conn, cur

def check_create_table(table_name):
  conn, cur = get_connection_cursor()

  # check and create table
  cur.execute(
    f'''
    select count(*) > 0
    from information_schema.tables
    where
      table_schema = 'source' and
      table_name ~ '^{table_name}'
    '''
  )
  if cur.fetchone()[0] is False:
    cur.execute(
      open(f'source_data/create-{table_name}.sql', 'r').read()
    )

def upload_game_info_to_database(game_schedules, season):
  table_name = 'game_info'

  # connect to DB
  conn, cur = get_connection_cursor()

  # check and create table
  check_create_table(table_name)

  # delete old rows
  cur.execute(
    f'delete from {table_name} where season = \'{season}\''
  )

  # upload data
  for game_schedule in game_schedules:
    cur.execute(
      f'''
      insert into {table_name} (game_id, season, date_time, league, stadium, home_team_id, home_team_name, home_score, away_team_id, away_team_name, away_score, exp_win)
      values (
        '{game_schedule['game_id']}',
        '{season}',
        '{game_schedule['date_time']}',
        '{game_schedule['league']}',
        '{game_schedule['stadium']}',
        {("'" + game_schedule['home_team_id'] + "'") if game_schedule['home_team_id'] is not None else 'NULL'},
        '{game_schedule['home_team_name'].replace("'","''")}',
        '{game_schedule['home_score']}',
        {("'" + game_schedule['away_team_id'] + "'") if game_schedule['away_team_id'] is not None else 'NULL'},
        '{game_schedule['away_team_name'].replace("'","''")}',
        '{game_schedule['away_score']}',
        {("'" + game_schedule['exp_win'] + "'") if game_schedule['exp_win'] is not None else 'NULL'}
      )
      '''
    )

def upload_player_info_to_database(player_infos):
  table_name = 'player_info'

  # connect to DB
  conn, cur = get_connection_cursor()

  # check and create table
  check_create_table(table_name)

  # delete old rows
  cur.execute(
    f'delete from {table_name}'
  )

  # upload data
  for player_info in player_infos:
    cur.execute(
      f'''
      insert into {table_name} (player_id, player_name, player_no, status, main_position, hand_type, team_id)
      values (
        '{player_info['player_id']}',
        '{player_info['player_name']}',
        '{player_info['player_no']}',
        '{player_info['status']}',
        {("'" + player_info['main_position'] + "'") if player_info['main_position'] is not None else 'NULL'},
        {("'" + player_info['hand_type'] + "'") if player_info['hand_type'] is not None else 'NULL'},
        '{player_info['team_id']}'
      )
      '''
    )

def upload_batter_by_game_to_database(batter_by_games, player_id, player_name, team_id, season):
  table_name = 'batter_by_game'

  # connect to DB
  conn, cur = get_connection_cursor()

  # check and create table
  check_create_table(table_name)

  # delete old rows
  cur.execute(
    f'delete from {table_name} where player_id = \'{player_id}\' and season = \'{season}\''
  )

  # upload data
  for batter_by_game in batter_by_games:
    cur.execute(
      f'''
      insert into {table_name} (player_id, player_name, team_id, season, date, lineup, position_code, avg, pa, ab, run, t_hit, hit1, hit2, hit3, hr, t_base, rbi, sb, cs, sh, sf, bb, ib, hp, kk, gd, slg, obp, sba, m_hit, ops, phhra, kk_bb, xbh_hit)
      values (
        '{player_id}',
        '{player_name}',
        '{team_id}',
        '{season}',
        '{batter_by_game['date']}',
        '{batter_by_game['lineup']}',
        '{batter_by_game['position_code']}',
        '{batter_by_game['avg']}',
        '{batter_by_game['pa']}',
        '{batter_by_game['ab']}',
        '{batter_by_game['run']}',
        '{batter_by_game['t_hit']}',
        '{batter_by_game['hit1']}',
        '{batter_by_game['hit2']}',
        '{batter_by_game['hit3']}',
        '{batter_by_game['hr']}',
        '{batter_by_game['t_base']}',
        '{batter_by_game['rbi']}',
        '{batter_by_game['sb']}',
        '{batter_by_game['cs']}',
        '{batter_by_game['sh']}',
        '{batter_by_game['sf']}',
        '{batter_by_game['bb']}',
        '{batter_by_game['ib']}',
        '{batter_by_game['hp']}',
        '{batter_by_game['kk']}',
        '{batter_by_game['gd']}',
        '{batter_by_game['slg']}',
        '{batter_by_game['obp']}',
        '{batter_by_game['sba']}',
        '{batter_by_game['m_hit']}',
        '{batter_by_game['ops']}',
        '{batter_by_game['phhra']}',
        '{batter_by_game['kk_bb']}',
        '{batter_by_game['xbh_hit']}'
      )
      '''
    )

def upload_batter_by_season_to_database(batter_by_season, player_id, player_name, team_id, season):
  table_name = 'batter_by_season'

  # connect to DB
  conn, cur = get_connection_cursor()

  # check and create table
  check_create_table(table_name)

  # delete old rows
  cur.execute(
    f'delete from {table_name} where player_id = \'{player_id}\' and season = \'{season}\''
  )

  # upload data
  cur.execute(
    f'''
    insert into {table_name} (player_id, player_name, team_id, season, t_game, avg, pa, ab, run, t_hit, hit1, hit2, hit3, hr, t_base, rbi, sb, cs, sh, sf, bb, ib, hp, kk, gd, slg, obp, sba, m_hit, ops, phhra, kk_bb, xbh_hit)
    values (
      '{player_id}',
      '{player_name}',
      '{team_id}',
      '{season}',
      '{batter_by_season['t_game']}',
      '{batter_by_season['avg']}',
      '{batter_by_season['pa']}',
      '{batter_by_season['ab']}',
      '{batter_by_season['run']}',
      '{batter_by_season['t_hit']}',
      '{batter_by_season['hit1']}',
      '{batter_by_season['hit2']}',
      '{batter_by_season['hit3']}',
      '{batter_by_season['hr']}',
      '{batter_by_season['t_base']}',
      '{batter_by_season['rbi']}',
      '{batter_by_season['sb']}',
      '{batter_by_season['cs']}',
      '{batter_by_season['sh']}',
      '{batter_by_season['sf']}',
      '{batter_by_season['bb']}',
      '{batter_by_season['ib']}',
      '{batter_by_season['hp']}',
      '{batter_by_season['kk']}',
      '{batter_by_season['gd']}',
      '{batter_by_season['slg']}',
      '{batter_by_season['obp']}',
      '{batter_by_season['sba']}',
      '{batter_by_season['m_hit']}',
      '{batter_by_season['ops']}',
      '{batter_by_season['phhra']}',
      '{batter_by_season['kk_bb']}',
      '{batter_by_season['xbh_hit']}'
    )
    '''
  )

def upload_pitcher_by_game_to_database(pitcher_by_games, player_id, player_name, team_id, season):
  table_name = 'pitcher_by_game'

  # connect to DB
  conn, cur = get_connection_cursor()

  # check and create table
  check_create_table(table_name)

  # delete old rows
  cur.execute(
    f'delete from {table_name} where player_id = \'{player_id}\' and season = \'{season}\''
  )

  # upload data
  for pitcher_by_game in pitcher_by_games:
    cur.execute(
      f'''
      insert into {table_name} (player_id, player_name, team_id, season, date, era, win, lose, save, hold, wra, pa, ab, bf, inn, hit, hr, sh, sf, bb, ibb, hp, kk, wp, bk, r, er, whip, oavg, k9k7)
      values (
        '{player_id}',
        '{player_name}',
        '{team_id}',
        '{season}',
        '{pitcher_by_game['date']}',
        '{pitcher_by_game['era']}',
        '{pitcher_by_game['win']}',
        '{pitcher_by_game['lose']}',
        '{pitcher_by_game['save']}',
        '{pitcher_by_game['hold']}',
        '{pitcher_by_game['wra']}',
        '{pitcher_by_game['pa']}',
        '{pitcher_by_game['ab']}',
        '{pitcher_by_game['bf']}',
        '{pitcher_by_game['inn']}',
        '{pitcher_by_game['hit']}',
        '{pitcher_by_game['hr']}',
        '{pitcher_by_game['sh']}',
        '{pitcher_by_game['sf']}',
        '{pitcher_by_game['bb']}',
        '{pitcher_by_game['ibb']}',
        '{pitcher_by_game['hp']}',
        '{pitcher_by_game['kk']}',
        '{pitcher_by_game['wp']}',
        '{pitcher_by_game['bk']}',
        '{pitcher_by_game['r']}',
        '{pitcher_by_game['er']}',
        '{pitcher_by_game['whip']}',
        '{pitcher_by_game['oavg']}',
        '{pitcher_by_game['k9k7']}'
      )
      '''
    )

def upload_pitcher_by_season_to_database(pitcher_by_season, player_id, player_name, team_id, season):
  table_name = 'pitcher_by_season'

  # connect to DB
  conn, cur = get_connection_cursor()

  # check and create table
  check_create_table(table_name)

  # delete old rows
  cur.execute(
    f'delete from {table_name} where player_id = \'{player_id}\' and season = \'{season}\''
  )

  cur.execute(
    f'''
    insert into {table_name} (player_id, player_name, team_id, season, t_game, era, win, lose, save, hold, wra, pa, ab, bf, inn, hit, hr, sh, sf, bb, ibb, hp, kk, wp, bk, r, er, whip, oavg, k9k7)
    values (
      '{player_id}',
      '{player_name}',
      '{team_id}',
      '{season}',
      '{pitcher_by_season['t_game']}',
      '{pitcher_by_season['era']}',
      '{pitcher_by_season['win']}',
      '{pitcher_by_season['lose']}',
      '{pitcher_by_season['save']}',
      '{pitcher_by_season['hold']}',
      '{pitcher_by_season['wra']}',
      '{pitcher_by_season['pa']}',
      '{pitcher_by_season['ab']}',
      '{pitcher_by_season['bf']}',
      '{pitcher_by_season['inn']}',
      '{pitcher_by_season['hit']}',
      '{pitcher_by_season['hr']}',
      '{pitcher_by_season['sh']}',
      '{pitcher_by_season['sf']}',
      '{pitcher_by_season['bb']}',
      '{pitcher_by_season['ibb']}',
      '{pitcher_by_season['hp']}',
      '{pitcher_by_season['kk']}',
      '{pitcher_by_season['wp']}',
      '{pitcher_by_season['bk']}',
      '{pitcher_by_season['r']}',
      '{pitcher_by_season['er']}',
      '{pitcher_by_season['whip']}',
      '{pitcher_by_season['oavg']}',
      '{pitcher_by_season['k9k7']}'
    )
    '''
  )
