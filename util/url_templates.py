__author__ = 'brycerich'

from string import Template

base_url = "https://statsapi.web.nhl.com"
scheduled_games_endpoint = Template(base_url+"/schedule?startDate=$startDate&endDate=$endDate")
nhl_schedule = base_url+"/api/v1/schedule"
nhl_game = Template(base_url+"/api/v1/game/$game_id/feed/live")
