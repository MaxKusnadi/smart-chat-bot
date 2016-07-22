from apiclient.discovery import build

import json


agent = build('customsearch', 'v1',
              developerKey="AIzaSyCf4gETs8Y4B7xz6XFiy_nJbOanIV2SyW4")


def searchGoogle(query):
    fullLink = agent.cse().list(
        q=query,
        cx="015262030262987356770:k0mimtodchc")
    response = fullLink.execute()
    try:
        ans = json.loads(response.decode("utf-8", errors="ignore"))
    except AttributeError:
        ans = json.loads(json.dumps(response))

    d = dict()
    abc = list()

    if (ans is not None):
        counter = 0
        for data in response.get("items", []):
            d['type'] = data["title"]
            try:
                d['text'] = data["pagemap"]["cse_image"][0]["src"]
            except:
                try:
                    d['text'] = data["pagemap"]["metatags"][0]["twitter:image"]
                except:
                    try:
                        d['text'] = data['pagemap']['cse_thumbnail'][0]\
                            ['src']
                    except:
                        d['text'] = ""
            counter += 1
            abc.append(d)
            if counter == 3:
                break
    else:
        d['type'] = "I don't understand your query"
        d['text'] = ''
        abc.append(d)

    return abc

if __name__ == '__main__':
    print(searchGoogle('Taylor Swift'))
