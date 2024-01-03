import requests, json


headers = {"Accept":"application/vnd.github+json","Authorization":"Bearer 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","X-GitHub-Api-Version":"2022-11-28"}
response = requests.get("https://api.github.com/repos/TeddyIIG/Portfolio/dependabot/alerts",headers=headers)
json_response = json.loads(response.text)
print(json_response)