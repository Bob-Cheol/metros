create table game_info (
  game_id varchar primary key,
  season varchar,
  date_time varchar,
  league varchar,
  stadium varchar,
  home_team_id varchar,
  home_team_name varchar,
  home_score numeric,
  away_team_id varchar,
  away_team_name varchar,
  away_score numeric,
  exp_win varchar,
  uploaded_at timestamp default current_timestamp
);
