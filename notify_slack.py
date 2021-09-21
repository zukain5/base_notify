import slackweb
from secret import SLACK_URL


def notify_slack(orders):
    slack = slackweb.Slack(url=SLACK_URL)
    