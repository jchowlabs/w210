#####################
# Tools, Tools, Tools
#####################

# This stanza imports the request library and browses
#(GET) the URL 100 times. The results are stored in a
# list and printed to retrieve the flag.
import requests as req

response_list = []

for i in range(100):
    resp = req.get("http://w210.network:8005/flag.txt")
    response_list.append(resp.text)
    i = i + 1
        
print(response_list)

