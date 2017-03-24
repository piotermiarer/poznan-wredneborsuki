import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = {
    'X-Auth-Token': '9df97b651e4244bbb8da6d50a6156d2b',
    'X-Response-Control': 'minified'
}
# should get next 7 fixtures
connection.request('GET', '/v1/fixtures', None, headers)
upcoming_fixtures = json.loads(connection.getresponse().read().decode())
# get some teams
leagues_with_teams = []
connection.request('GET', '/v1/competitions/', None, headers)
league_list = json.loads(connection.getresponse().read().decode())
for league in league_list:
    leagues_with_teams.append({})
    leagues_with_teams[-1]["name"] = league["caption"]
    leagues_with_teams[-1]["teams"] = []
    url = '/v1/competitions/'+ str(league["id"]) + '/teams'
    connection.request('GET', url, None, headers)
    teams_in_league = json.loads(connection.getresponse().read().decode())
    for team in teams_in_league["teams"]:
        team = {"name": team["name"], "crest_url": team["crestUrl"]}
        leagues_with_teams[-1]["teams"].append(team)
