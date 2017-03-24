import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': '9df97b651e4244bbb8da6d50a6156d2b',
            'X-Response-Control': 'minified' }
# should get next 7 fixtures
connection.request( 'GET', '/v1/fixtures', None, headers )
upcoming_fixtures = json.loads(connection.getresponse().read().decode())
# get some teams
leages_with_teams = []
connection.request( 'GET', '/v1/competitions/', None, headers )
leage_table = json.loads(connection.getresponse().read().decode())
i=0
for league in leage_table:
    leages_with_teams.append({})
    leages_with_teams[i]["name"] = league["caption"]
    leages_with_teams[i]["teams"] = []
    url = '/v1/competitions/'+ str(league["id"]) + '/teams'
    connection.request( 'GET', url, None, headers )
    teams_in_leage = json.loads(connection.getresponse().read().decode())
    for team in teams_in_leage["teams"]:
        team = {"name": team["name"], "crest_url": team["crestUrl"]}
        leages_with_teams[i]["teams"].append(team)
    i += 1

print(leages_with_teams)
