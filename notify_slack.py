import slackweb
from orders import sum_of_earnings
from secret import SLACK_URL


def notify_slack(orders):
    if len(orders) == 0:
        return

    slack = slackweb.Slack(url=SLACK_URL)
    text = f'昨日の売上は{sum_of_earnings(orders)}円！'
    slack.notify(text=text)

    return
