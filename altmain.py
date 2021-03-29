import os
from slack_sdk import WebClient

client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
response = client.api_call(
    api_method='chat.postMessage',
    json={'channel': '#updates','text': "Hello world!"}
)
assert response["message"]["text"] == "Hello world!"
