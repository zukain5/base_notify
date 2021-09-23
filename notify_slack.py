import slackweb
from orders import sum_of_earnings
from secret import SLACK_URL
from settings import notify_when_no_order


def notify_slack(orders):
    if len(orders) == 0 and not notify_when_no_order:
        return

    slack = slackweb.Slack(url=SLACK_URL)
    text = f'昨日の売上は{sum_of_earnings(orders)}円！'
    slack.notify(text=text)

    return
