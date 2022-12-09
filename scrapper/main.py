from requests import get
from bs4 import BeautifulSoup
from extractors.scraper_for_team_game_record import extract_boxscore

extract_boxscore('metros', 'test')
