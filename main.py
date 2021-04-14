import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


while True:
    try:
        filepath="./TemperatureData.csv"
        response = client.files_upload(channels='#updates', file=filepath)
        assert response["file"]  # the uploaded file
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")
    time.sleep(3600)