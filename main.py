import json

from bs4 import BeautifulSoup
import requests

import constants

res = requests.get(url=constants.CAR_MAKE_URL, headers= constants.CAR_MAKE_HEADER)
data = json.loads(res.content)
print(data["data"]["makes"])

# json -> data -> makes -> 0 -> dict(key, doc_count)

# per page 10 info
# max of 30 pages use min to confirm:


"https://api.terrific.ie/api/ad-elastic-filters?quickSearch=1&makes=audi"