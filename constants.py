HEADERS = {
    "accept": "application/json, text/plain, */*", 
    "accept-encoding": "gzip, deflate, zstd", 
    "accept-language": "en-US,en;q=0.9,ta;q=0.8", 
    "dnt": "1", 
    "origin": "https://www.terrific.ie", 
    "priority": "u=1, i",
    "referer": "https://www.terrific.ie/",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
}

CAR_MAKE_URL = "https://api.terrific.ie/api/ad-elastic-filters"

CAR_MODEL_URL = "https://api.terrific.ie/api/ad-elastic-filters?quickSearch=1&makes={make}"

CAR_URL_WITHOUT_MODEL = "https://api.terrific.ie/api/ad-elastic-filters?&makes={make}&page={page_no}" # without model
CAR_URL_WITH_MODEL = "https://api.terrific.ie/api/ad-elastic-filters?&makes={make}&models={model}&page={page_no}" # with model