from requests import get
from bs4 import BeautifulSoup

def extract_game_boxscores(club_idx, game_idx):
  print(club_idx, game_idx)
