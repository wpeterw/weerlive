from weerlive import WeerLive

weer_live = WeerLive(api_key="demo", location="Amsterdam")

weer = weer_live.get_live_weather()

print(weer.current_temperature)