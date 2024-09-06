import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

    response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")
    print(response.json())
else:
    print("Received number of arguments does not equal 2")
    print(sys.argv)
