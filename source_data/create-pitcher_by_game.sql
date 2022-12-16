create table pitcher_by_game (
  player_id varchar,
  player_name varchar,
  team_id varchar,
  season varchar,
  date varchar,
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
comment on column pitcher_by_game.player_id is '선수 ID';
comment on column pitcher_by_game.player_name is '선수 이름';
comment on column pitcher_by_game.team_id is '팀 ID';
comment on column pitcher_by_game.season is '시즌';
comment on column pitcher_by_game.date is '일자';
comment on column pitcher_by_game.era is '방어율';
comment on column pitcher_by_game.win is '승';
comment on column pitcher_by_game.lose is '패';
comment on column pitcher_by_game.save is '세';
comment on column pitcher_by_game.hold is '홀드';
comment on column pitcher_by_game.wra is '승률';
comment on column pitcher_by_game.pa is '타자';
comment on column pitcher_by_game.ab is '타수';
comment on column pitcher_by_game.bf is '투구수';
comment on column pitcher_by_game.inn is '이닝';
comment on column pitcher_by_game.hit is '피안타';
comment on column pitcher_by_game.hr is '피홈런';
comment on column pitcher_by_game.sh is '희타';
comment on column pitcher_by_game.sf is '희비';
comment on column pitcher_by_game.bb is '볼넷';
comment on column pitcher_by_game.ibb is '고의4구';
comment on column pitcher_by_game.hp is '사구';
comment on column pitcher_by_game.kk is '탈삼진';
comment on column pitcher_by_game.wp is '폭투';
comment on column pitcher_by_game.bk is '보크';
comment on column pitcher_by_game.r is '실점';
comment on column pitcher_by_game.er is '자책점';
comment on column pitcher_by_game.whip is 'WHIP';
comment on column pitcher_by_game.oavg is '피안타율';
comment on column pitcher_by_game.k9k7 is '탈삼진율';
