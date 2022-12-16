create table batter_by_season (
  player_id varchar,
  player_name varchar,
  team_id varchar,
  season varchar,
  t_game numeric,
  avg numeric,
  pa numeric,
  ab numeric,
  run numeric,
  t_hit numeric,
  hit1 numeric,
  hit2 numeric,
  hit3 numeric,
  hr numeric,
  t_base numeric,
  rbi numeric,
  sb numeric,
  cs numeric,
  sh numeric,
  sf numeric,
  bb numeric,
  ib numeric,
  hp numeric,
  kk numeric,
  gd numeric,
  slg numeric,
  obp numeric,
  sba numeric,
  m_hit numeric,
  ops numeric,
  phhra numeric,
  kk_bb numeric,
  xbh_hit numeric,
  uploaded_at timestamp default current_timestamp
);
comment on column batter_by_season.player_id is '선수 ID';
comment on column batter_by_season.player_name is '선수 이름';
comment on column batter_by_season.team_id is '팀 ID';
comment on column batter_by_season.season is '시즌';
comment on column batter_by_season.t_game is '총경기';
comment on column batter_by_season.avg is '타율';
comment on column batter_by_season.pa is '타석';
comment on column batter_by_season.ab is '타수';
comment on column batter_by_season.run is '득점';
comment on column batter_by_season.t_hit is '총안타';
comment on column batter_by_season.hit1 is '1루타';
comment on column batter_by_season.hit2 is '2루타';
comment on column batter_by_season.hit3 is '3루타';
comment on column batter_by_season.hr is '홈런';
comment on column batter_by_season.t_base is '루타';
comment on column batter_by_season.rbi is '타점';
comment on column batter_by_season.sb is '도루';
comment on column batter_by_season.cs is '도실(도루자)';
comment on column batter_by_season.sh is '희타';
comment on column batter_by_season.sf is '희비';
comment on column batter_by_season.bb is '볼넷';
comment on column batter_by_season.ib is '고의4구';
comment on column batter_by_season.hp is '사구(死구)';
comment on column batter_by_season.kk is '삼진';
comment on column batter_by_season.gd is '병살';
comment on column batter_by_season.slg is '장타율';
comment on column batter_by_season.obp is '출루율';
comment on column batter_by_season.sba is '도루성공률';
comment on column batter_by_season.m_hit is '멀티히트';
comment on column batter_by_season.ops is 'OPS';
comment on column batter_by_season.phhra is '대타타율';
comment on column batter_by_season.kk_bb is 'BB/K';
comment on column batter_by_season.xbh_hit is '장타/안타';
