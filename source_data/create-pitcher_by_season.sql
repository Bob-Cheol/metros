create table pitcher_by_season (
  player_id varchar,
  player_name varchar,
  team_id varchar,
  season varchar,
  t_game numeric,
  era numeric,
  win numeric,
  lose numeric,
  save numeric,
  hold numeric,
  wra numeric,
  pa numeric,
  ab numeric,
  bf numeric,
  inn numeric,
  hit numeric,
  hr numeric,
  sh numeric,
  sf numeric,
  bb numeric,
  ibb numeric,
  hp numeric,
  kk numeric,
  wp numeric,
  bk numeric,
  r numeric,
  er numeric,
  whip numeric,
  oavg numeric,
  k9k7 numeric,
  uploaded_at timestamp default current_timestamp
);
comment on column pitcher_by_season.player_id is '선수 ID';
comment on column pitcher_by_season.player_name is '선수 이름';
comment on column pitcher_by_season.team_id is '팀 ID';
comment on column pitcher_by_season.season is '시즌';
comment on column pitcher_by_season.t_game is '총경기';
comment on column pitcher_by_season.era is '방어율';
comment on column pitcher_by_season.win is '승';
comment on column pitcher_by_season.lose is '패';
comment on column pitcher_by_season.save is '세';
comment on column pitcher_by_season.hold is '홀드';
comment on column pitcher_by_season.wra is '승률';
comment on column pitcher_by_season.pa is '타자';
comment on column pitcher_by_season.ab is '타수';
comment on column pitcher_by_season.bf is '투구수';
comment on column pitcher_by_season.inn is '이닝';
comment on column pitcher_by_season.hit is '피안타';
comment on column pitcher_by_season.hr is '피홈런';
comment on column pitcher_by_season.sh is '희타';
comment on column pitcher_by_season.sf is '희비';
comment on column pitcher_by_season.bb is '볼넷';
comment on column pitcher_by_season.ibb is '고의4구';
comment on column pitcher_by_season.hp is '사구';
comment on column pitcher_by_season.kk is '탈삼진';
comment on column pitcher_by_season.wp is '폭투';
comment on column pitcher_by_season.bk is '보크';
comment on column pitcher_by_season.r is '실점';
comment on column pitcher_by_season.er is '자책점';
comment on column pitcher_by_season.whip is 'WHIP';
comment on column pitcher_by_season.oavg is '피안타율';
comment on column pitcher_by_season.k9k7 is '탈삼진율';
