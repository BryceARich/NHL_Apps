__author__ = 'brycerich'
from led_scoreboard import LedScoreboard
from endpoint_manager import EndpointManager
from json_scraper import get_score, get_teams, check_if_scoring_play, get_play_summary,\
get_time_remaining

if __name__ == '__main__':
    sb = LedScoreboard()
    epm = EndpointManager()

    date_range = {'startDate': "2017-09-17",
                  'endDate': "2017-09-17"}
    payload = epm.get_date_range_games(date_range)

    for date in payload.get('dates'):
        for game in date.get('games'):
            game_id = "2017021266"
##            game_id = game.get('gamePk')
            game_events = epm.get_game_events(game_id)
            home_team, away_team = get_teams(game_events)
            sb.set_home_team(home_team)
            sb.set_away_team(away_team)
            try:
                score = get_score(game_events,0)
            except:
                print("Error with game")
                continue
            home_team, away_team = get_teams(game_events)
            print(away_team + " vs " + home_team)
            print(score)
            sb.set_score(score)
            for i in range(len(game_events.get('liveData').get('plays').get('allPlays'))):
                game_events = epm.get_game_events(game_id)
                goal, team = check_if_scoring_play(game_events,i)
                ordinal, remaining = get_time_remaining(game_events,i)
                sb.set_time(ordinal, remaining)
                if goal:
                    description = get_play_summary(game_events, i)
                    score = get_score(game_events, i)
                    sb.set_score(score)
                    if away_team in team:
                        team = away_team
                        print("%s SCORE" % away_team)
                        description = ("%s GOAL!!! " + description)% away_team
                    else:
                        team = home_team
                        print("%s SCORE" % home_team)
                        description = ("%s GOAL!!! " + description)% home_team
                    sb.display_play_description(description,team)
                    print(score)
