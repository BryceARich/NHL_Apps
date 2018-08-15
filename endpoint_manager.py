__author__ = 'brycerich'
import requests, json, datetime
from util.url_templates import scheduled_games_endpoint, nhl_schedule

class EndpointManager:

    def get_todays_games(self):
        """
        Gets the endpoint for today's games
        :return:
        """
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        date_range = {'startDate': today,
                      'endDate': today}
        return self.get_date_range_games(date_range)

    def get_date_range_games(self, date_range):
        """
        Gives date range of games
        :param date_range: dict with startDate and endDate to find games over
        :return:
        """
        return json.loads(requests.get(nhl_schedule, date_range).content.decode("utf-8"))


if __name__ == '__main__':
    epm = EndpointManager()
    date_range = {'startDate': "2018-09-15",
                  'endDate': "2018-09-15"}
    payload = epm.get_date_range_games(date_range)
    # payload = epm.get_todays_games()
    for date in payload.get('dates'):
        for game in date.get('games'):
            print(game.keys())
            print(game.get('gamePk'))
            print(game.get('status'))
            print(game.get('gameDate'))
            print(game.get('gameDate') < datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'))

