# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

#This url is from the Jira account till .net and rest is same
url = "https://madireddy008.atlassian.net/rest/api/3/project"

#this API token is from the our Jira account link to create API token:https://id.atlassian.com/manage-profile/security/api-tokens
API_TOKEN = "ATATT3xFfGF0PtrgZY5M8Ur9avIQzBo_DZnyJpzK4iLQDV4w0MNlmEp2GVcBFvM85vSocatoPsVX8dnKb1I5h_T9Te3ZZFkFE6em2D4rH738JCwuEM9r_Q-OC-AIcllDD89pqmvXc70nlFN6pJlvI3Xz4DLMe0SAu7N-A6AQGgO2g7KehnL4iho=C4252C74"
EMAIL = "madireddyanilkumarreddy008@gmail.com"
auth = HTTPBasicAuth(EMAIL, API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)


#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
outputs = json.loads(response.text)

#here we will write a code in for loop to iterate through the outputs and filter the project names and display them in output
for output in outputs:
    for key,value in output.items():
        #print(key,":",value)
        if key == "name":
            print("Project_Name:", value)