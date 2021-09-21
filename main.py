from get_access_token import get_access_token
from orders import get_orders
from notify_slack import notify_slack
import datetime


def main():
    access_token = get_access_token()

    today = datetime.datetime.today()
    td = datetime.timedelta(days=1)
    yesterday = today - td

    y = yesterday.year
    m = yesterday.month
    d = yesterday.day

    start = datetime.datetime(y, m, d, 0, 0, 0)
    end = datetime.datetime(y, m, d, 23, 59, 59)

    orders = get_orders(start, end, access_token)
    notify_slack(orders)


if __name__ == '__main__':
    main()
