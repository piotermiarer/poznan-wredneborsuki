import http.client
import json

def get_upcoming():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {
        'X-Auth-Token': '9df97b651e4244bbb8da6d50a6156d2b',
        'X-Response-Control': 'minified'
    }
    # should get next 7 fixtures
    connection.request('GET', '/v1/fixtures?timeFrame=n10&league=PL,BL1,SA,PD,FL1,DED,PPL', None, headers)
    upcoming_fixtures = json.loads(connection.getresponse().read().decode())

    # get team names from upcoming_fixtures
    upcoming_teams = []
    for fixture in upcoming_fixtures["fixtures"]:
        upcoming_teams.append(fixture["homeTeamName"])
        upcoming_teams.append(fixture["awayTeamName"])

    return upcoming_fixtures, upcoming_teams
