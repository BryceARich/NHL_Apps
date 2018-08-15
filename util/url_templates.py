__author__ = 'brycerich'

from string import Template

base_url = "https://statsapi.web.nhl.com/api/v1"
scheduled_games_endpoint = Template(base_url+"/schedule?startDate=$startDate&endDate=$endDate")
nhl_schedule = base_url+"/schedule"
