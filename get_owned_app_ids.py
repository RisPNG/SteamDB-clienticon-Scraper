import requests
import json

# Replace with your Steam Web API key and Steam ID
# Steam Web API Key: https://steamcommunity.com/dev/apikey
# Steam64 ID / steamID64: https://steamid.xyz/
STEAM_WEB_API_KEY = "Steam_Web_API_Key"
STEAM64_ID = "76561198028632468"

# Steam API endpoint to get owned games
STEAM_API_ENDPOINT = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"

# Parameters for the API request
params = {
    "key": STEAM_WEB_API_KEY,
    "steamid": STEAM64_ID,
    "include_appinfo": "1",  # Include app info
    "include_played_free_games": "1",  # Include free games
    "format": "json"
}

# Make the API request
response = requests.get(STEAM_API_ENDPOINT, params=params)
response.raise_for_status()  # Raise an exception for bad status codes

# Parse the JSON response
data = response.json()

# Extract the list of owned games and write to a file
if "response" in data and "games" in data["response"]:
    owned_games = data["response"]["games"]
    with open("owned_app_ids.txt", "w", encoding="utf-8") as outfile:
        for game in owned_games:
            outfile.write(f"{game['appid']}\n")
    print("AppIDs saved to owned_app_ids.txt")
else:
    print("No games found or error in API response")
