__author__ = 'brycerich'
import requests, json, datetime
from util.url_templates import scheduled_games_endpoint, nhl_schedule, nhl_game, base_url

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

    @staticmethod
    def get_date_range_games(date_range):
        """
        Gives date range of games
        :param date_range: dict with startDate and endDate to find games over
        :return:
        """
        return json.loads(requests.get(nhl_schedule, date_range).content.decode("utf-8"))

    @staticmethod
    def get_game_events(game_id):
        """
        Gets the full json for a provided game_id
        :param game_id:
        :return:
        """
        return json.loads(requests.get(nhl_game.substitute(game_id=game_id)).content.decode("utf-8"))

    @staticmethod
    def get_json_from_endpoint(endpoint):
        """
        Gets the full json for a provided endpoint (suggested use with a known link from elsewhere in site)
        :param endpoint:
        :return:
        """
        print(base_url+endpoint)
        return json.loads(requests.get(base_url+endpoint).content.decode("utf-8"))


if __name__ == '__main__':
    epm = EndpointManager()
    date_range = {'startDate': "2017-09-16",
                  'endDate': "2017-09-16"}
    payload = epm.get_date_range_games(date_range)
    # payload = epm.get_todays_games()
    for date in payload.get('dates'):
        for game in date.get('games'):
            game_id = game.get('gamePk')
            game_events = epm.get_game_events(game_id)
            score = game_events.get('liveData').get('plays').get('allPlays')[0].get('about').get('goals')
            away_team = game_events.get('gameData').get('teams').get('away').get('teamName')
            home_team = game_events.get('gameData').get('teams').get('home').get('teamName')
            print(away_team)
            print(home_team)
            print(score)
            for i in range(len(game_events.get('liveData').get('plays').get('allPlays'))):
                game_events = epm.get_game_events(game_id)
                # print(game_events.keys())
                # gameData = game_events.get('gameData')
                # print(gameData.keys())
                # print(gameData.get('teams'))
                liveData = game_events.get('liveData')
                # print(liveData.keys())
                plays = liveData.get('plays')
                # print(plays.keys())
                # print(plays.get('scoringPlays')) #can utilize this to know if score is different than it was before
                if i in plays.get('scoringPlays'):

                    new_score = plays.get('allPlays')[i].get('about').get('goals')
                    if(new_score.get('away') > score.get('away')):
                        print("%s SCORE" % away_team)
                    else:
                        print("%s SCORES" % home_team)
                    print(new_score)
                    score = new_score
                # else:
                #     print('...%s' % i)
                # for scoring_play in plays.get('scoringPlays'):
                #     print(plays.get('allPlays')[scoring_play])
                #     print(plays.get('allPlays')[scoring_play].get('about').get('goals'))
                # print(game.keys())
                # print(game.get('gamePk'))
                # print(game.get('status'))
                # print(game.get('gameDate'))
                # print(game.get('gameDate') < datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'))

