import requests
import json


def dt_to_str(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def get_orders(start_ordered, end_ordered, access_token):
    req_path = 'https://api.thebase.in/1/orders'

    params = {
        'start_ordered': dt_to_str(start_ordered),
        'end_ordered': dt_to_str(end_ordered),
        'limit': 100,
        'offset': 0,
    }

    header = {
        "Authorization": "Bearer " + access_token,
    }

    res = requests.get(req_path, params=params, headers=header)
    orders_data = json.loads(res.text)

    return orders_data['orders']


def sum_of_earnings(orders):
    earnings = 0
    for order in orders:
        earnings += order['total']

    return earnings
