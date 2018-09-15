__author__ = 'brycerich'
from led_scoreboard import LedScoreboard
from endpoint_manager import EndpointManager
from json_scraper import get_score, get_teams, check_if_scoring_play

if __name__ == '__main__':
    sb = LedScoreboard()
    epm = EndpointManager()

    date_range = {'startDate': "2017-09-17",
                  'endDate': "2017-09-21"}
    payload = epm.get_date_range_games(date_range)

    for date in payload.get('dates'):
        for game in date.get('games'):
            ##game_id = "2017021266"
            game_id = game.get('gamePk')
            game_events = epm.get_game_events(game_id)
            home_team, away_team = get_teams(game_events)
            sb.set_home_team(home_team.split(" ")[-1])
            sb.set_away_team(away_team.split(" ")[-1])
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
                if goal:
                    score = get_score(game_events, i)
                    if team == away_team:
                        print("%s SCORE" % away_team)
                    else:
                        print("%s SCORE" % home_team)
                    sb.set_score(score)
                    print(score)

    sb.root.mainloop()