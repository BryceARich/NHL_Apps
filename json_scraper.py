__author__ = 'brycerich'

# class JsonScraper:
#     """
#     All functions in this class assume they are getting data from the feed/live endpoint unless otherwise specified
#     """

def get_teams(json):
    """
    Obtains the teams in a particular live feed
    :param json:
    :return: tuple containing (home_team, away_team)
    """
    home_team = json.get('gameData').get('teams').get('home').get('teamName')
    away_team = json.get('gameData').get('teams').get('away').get('teamName')
    return (home_team, away_team)

def get_score(json, play_number=-1):
    return json.get('liveData').get('plays').get('allPlays')[play_number].get('about').get('goals')

def get_play_summary(json, play_number=-1):
    return json.get('liveData').get('plays').get('allPlays')[play_number].get('result').get('description')

def check_if_scoring_play(json, play_number=-1):
    is_scoring_play = False
    scoring_team = ''
    plays = json.get('liveData').get('plays')
    if(play_number != -1):
        if(play_number in plays.get("scoringPlays")):
            is_scoring_play = True
            scoring_team = plays.get('allPlays')[play_number].get('team').get('name')
    else:
        num_plays = len(plays.get('allPlays'))
        if(num_plays-1 in plays.get("scoringPlays")):
            is_scoring_play = True
            scoring_team = plays.get('allPlays')[play_number].get('team').get('name')
    return (is_scoring_play, scoring_team)

def get_time_remaining(json, play_number=-1):
    plays = json.get('liveData').get('plays')
    ordinal = plays.get('allPlays')[play_number].get('about').get('ordinalNum')
    remaining = plays.get('allPlays')[play_number].get('about').get('periodTimeRemaining')
    return (ordinal, remaining)

if __name__ == '__main__':
    list = [1,2,3,4,5]


