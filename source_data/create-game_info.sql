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
comment on column game_info.game_id is '경기 ID';
comment on column game_info.season is '시즌';
comment on column game_info.date_time is '일시';
comment on column game_info.league is '리그';
comment on column game_info.stadium is '구장';
comment on column game_info.home_team_id is '홈팀 ID';
comment on column game_info.home_team_name is '홈팀 이름';
comment on column game_info.home_score is '홈팀 점수';
comment on column game_info.away_team_id is '어웨이팀 ID';
comment on column game_info.away_team_name is '어웨이팀 이름';
comment on column game_info.away_score is '어웨이팀 점수';
comment on column game_info.exp_win is '부가사항';
