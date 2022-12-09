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
