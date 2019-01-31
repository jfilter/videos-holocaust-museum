import re
from pathlib import Path

from requests_html import HTMLSession

# adapt search string here for your needs
base_url = "https://collections.ushmm.org/search/?Accession+Number=&Author=&Call+Number=&Category=&Classification=&Date=&Film+ID=&Film+Source=&Funding+Note=&Locale=&Object+Type=&Parent+Catalog+ID=&Photo+%2F+Film+Keyword=&Photo+Caption=&Photo+Designation=&Photo+Number=&Provenance=&Publication+Year=&RG+Number=&Subject=&Title=&f%5Bavailability%5D%5B%5D=digitized&f%5Bf_audiovisual%5D%5B%5D=historic_film&op=AND&q=hitler+speech&search_field=all_fields&sort=score+desc"

videos = []
session = HTMLSession()
page = 0

while True:
    url = f"{base_url}&page={page}"
    print("get :", url)
    r = session.get(url)

    links = r.html.absolute_links

    links = [
        l
        for l in links
        if re.match(r"^https://collections.ushmm.org/search/catalog/[a-z0-9]*$", l)
    ]

    print(len(links))

    if len(links) == 0:
        print("done")
        break

    for l in links:
        r = session.get(l)
        print(l)

        for m in set(
            list(
                re.findall(
                    r"https:\/\/film-assets\.ushmm\.org\/mp4\/.*\.mp4", r.html.html
                )
            )
        ):
            videos.append(m)
            print(m)

    page += 1

Path("urls.txt").write_text("\n".join(videos))
