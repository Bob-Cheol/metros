create table player_info (
  player_id varchar primary key,
  player_name varchar,
  player_no numeric,
  status varchar,
  main_position varchar,
  hand_type varchar,
  team_id varchar,
  uploaded_at timestamp default current_timestamp
);
comment on column player_info.player_id is '선수 ID';
comment on column player_info.player_name is '선수 이름';
comment on column player_info.player_no is '선수 번호';
comment on column player_info.status is '활동상태';
comment on column player_info.main_position is '주포지션';
comment on column player_info.hand_type is '핸드타입';
comment on column player_info.team_id is '팀 ID';
