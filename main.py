import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token='xoxb-1868163589349-1924651479234-FhgM9SfZXngOBxME0HeiDcX7')

try:
    response = client.chat_postMessage(channel='#updates', text="Save the Bees!")
    assert response["message"]["text"] == "Save the Bees!"
except SlackApiError as e:
    assert e.response["ok"] is False
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")