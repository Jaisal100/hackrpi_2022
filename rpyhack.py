import requests
import json

''''''
api_url1 = "https://api.spacexdata.com/v5/launches/latest"
response1 = requests.get(api_url1)
response1.json()

response1 = requests.get(api_url1)

data1=response1.text

parse_json1=json.loads(data1)

''''''
rocket=parse_json1['rocket']
launchpad=parse_json1['launchpad']

''''''
api_url2 = "https://api.spacexdata.com/v4/rockets/{}".format(rocket)
response2 = requests.get(api_url2)
response2.json()

response1 = requests.get(api_url2)

data2=response2.text

parse_json2=json.loads(data2)

''''''
api_url3 = "https://api.spacexdata.com/v4/launchpads/{}".format(launchpad)
response3 = requests.get(api_url3)
response3.json()

response3 = requests.get(api_url3)

data3=response3.text

parse_json3=json.loads(data3)

''''''

latest_flight=str(parse_json1['flight_number'])
print(latest_flight)
mission_name=parse_json1['name']
print(mission_name)
launch_date=parse_json1['date_local'][:10]
launch_date=launch_date[5:]+"-"+launch_date[:4]
print(launch_date)
youtube_video=parse_json1['links']['youtube_id']
youtube_video="http://www.youtube.com/watch?v="+youtube_video
print(youtube_video)
rocket_name=parse_json2['name']
print(rocket_name)
rocket_success_rate=parse_json2['success_rate_pct']
rocket_success_rate=('{:}%'.format(rocket_success_rate))
print(rocket_success_rate)
launchpad_name=parse_json3['full_name']
print(launchpad_name)
launchpad_success_rate=int(((int(parse_json3['launch_successes'])/int(parse_json3['launch_attempts']))*100))
launchpad_success_rate="{:}%".format(launchpad_success_rate)
print(launchpad_success_rate)


# Launch
f1=open('f1.txt','w')
f1.write(latest_flight)

f2=open('f2.txt','w')
f2.write(mission_name)

f3=open('f3.txt','w')
f3.write(launch_date)

f4=open('f4.txt','w')
f4.write(youtube_video)

# Rocket
f5=open('f5.txt','w')
f5.write(rocket_name)

f6=open('f6.txt','w')
f6.write(rocket_success_rate)

# Launchpad
f7=open('f7.txt','w')
f7.write(launchpad_name)

f8=open('f8.txt','w')
f8.write(launchpad_success_rate)