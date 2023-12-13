import requests
import sys

if len(sys.argv) != 2:
        sys.exit()
# url original: https://itunes.apple.com/search?entity=song&limit=1&term=weezer
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

print(response.json())