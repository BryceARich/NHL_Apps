__author__ = 'brycerich'

class JsonScraper:
    """
    All functions in this class assume they are getting data from the feed/live endpoint unless otherwise specified
    """

    def get_teams(self, json):
        """
        Obtains the teams in a particular live feed
        :param json:
        :return: tuple containing (home_team, away_team)
        """
        home_team = json.get('gameData').get('teams').get('home').get('teamName')
        away_team = json.get('gameData').get('teams').get('away').get('teamName')
        return (home_team, away_team)

    def check_if_scoring_play(self, json, play_number=-1):
        scoring_play = False
        plays = json.get('liveData').get('plays')
        if(play_number != -1):
            scoring_play = play_number in plays.get("scoringPlays")


