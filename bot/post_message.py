import os
from slack import WebClient
from dotenv import load_dotenv
from bot.builder import construct_payload
from utils.random_quote  import random_quotes_generator

load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# Initialize a Web API client
slack_web_client = WebClient(token=SLACK_BOT_TOKEN)


def post_quote_to_channel():
    quote = random_quotes_generator()
    author = quote['author']
    link = f"https://www.brainyquote.com{quote['author-link']}"


    # Get the onboarding message payload
    message = construct_payload({
        "type": "section",
        "text": {
                "type": "mrkdwn",
                "text": "*Your daily dose of motivation* :blush:"
        }
    },
        {
        "type": "divider"
    },
        {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"The test of the artist does not lie in the will with which he goes to work, but in the excellence of the work he produces... *By <{link}|{author}>*"
        }
    })
    # Post the onboarding message in Slack
    response = slack_web_client.chat_postMessage(**message)
