create table batter_by_game (
  player_id varchar,
  player_name varchar,
  team_id varchar,
  season varchar,
  date varchar,
  lineup varchar,
  position_code varchar,
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
comment on column batter_by_game.player_id is '선수 ID';
comment on column batter_by_game.player_name is '선수 이름';
comment on column batter_by_game.team_id is '팀 ID';
comment on column batter_by_game.season is '시즌';
comment on column batter_by_game.date is '일자';
comment on column batter_by_game.lineup is '타순';
comment on column batter_by_game.position_code is '포지션';
comment on column batter_by_game.avg is '타율';
comment on column batter_by_game.pa is '타석';
comment on column batter_by_game.ab is '타수';
comment on column batter_by_game.run is '득점';
comment on column batter_by_game.t_hit is '총안타';
comment on column batter_by_game.hit1 is '1루타';
comment on column batter_by_game.hit2 is '2루타';
comment on column batter_by_game.hit3 is '3루타';
comment on column batter_by_game.hr is '홈런';
comment on column batter_by_game.t_base is '루타';
comment on column batter_by_game.rbi is '타점';
comment on column batter_by_game.sb is '도루';
comment on column batter_by_game.cs is '도실(도루자)';
comment on column batter_by_game.sh is '희타';
comment on column batter_by_game.sf is '희비';
comment on column batter_by_game.bb is '볼넷';
comment on column batter_by_game.ib is '고의4구';
comment on column batter_by_game.hp is '사구(死구)';
comment on column batter_by_game.kk is '삼진';
comment on column batter_by_game.gd is '병살';
comment on column batter_by_game.slg is '장타율';
comment on column batter_by_game.obp is '출루율';
comment on column batter_by_game.sba is '도루성공률';
comment on column batter_by_game.m_hit is '멀티히트';
comment on column batter_by_game.ops is 'OPS';
comment on column batter_by_game.phhra is '대타타율';
comment on column batter_by_game.kk_bb is 'BB/K';
comment on column batter_by_game.xbh_hit is '장타/안타';
