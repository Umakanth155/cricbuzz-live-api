import requests
from bs4 import BeautifulSoup

def fetch_live_scores():
    url = "https://www.cricbuzz.com/cricket-match/live-scores"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    matches = []
    match_blocks = soup.select(".cb-col.cb-col-100.cb-ltst-wgt-hdr")  # main container

    for block in match_blocks:
        title_tag = block.select_one(".cb-ovr-flo.cb-hmscg-tm-nm")
        score_tag = block.select_one(".cb-ovr-flo.cb-text-live")
        status_tag = block.select_one(".cb-text-complete, .cb-text-live")

        if title_tag and score_tag and status_tag:
            match_info = {
                "match": title_tag.text.strip(),
                "score": score_tag.text.strip(),
                "status": status_tag.text.strip()
            }
            matches.append(match_info)

    return matches
