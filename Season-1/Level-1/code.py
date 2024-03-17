'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_PRICE_AMOUNT = 100_000
MIN_ARTICLE_AMOUNT = 0
MAX_ARTICLE_AMOUNT = 100

def validorder(order: Order):
    payment = 0
    debt = 0
    for item in order.items:
        is_in_range = -MAX_PRICE_AMOUNT < item.amount <= MAX_PRICE_AMOUNT
        if item.type == 'payment':
            if is_in_range:
                debt += item.amount
        elif item.type == 'product':
            if item.quantity > MIN_ARTICLE_AMOUNT and item.quantity <= MAX_ARTICLE_AMOUNT and is_in_range:
                payment -= item.amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type

    if  payment > MAX_PRICE_AMOUNT or debt > MAX_PRICE_AMOUNT:
        return "Total amount payable for an order exceeded"
    net = debt + payment
    if abs(net) > 0.00001:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id