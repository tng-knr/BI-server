""" Transactions helpers"""
import os
import requests
import datetime
import math
from dateutil.relativedelta import relativedelta
from django.shortcuts import get_object_or_404

from src.api.models import Transaction, IncomeStream

transactions_url = os.getenv('TRANSACTONS_URL')
cred = os.getenv('CRED')


def get_transactions(revenue_stream):
    """Get transactions from a third party api and populate our db"""
    prev_trans = 0
    try:
        response = requests.get(transactions_url,auth=(cred, cred))
    except Exception as err:
        print(err)
    for res in response.json()['results']:
        for item in res['results']:
            transactions = item['items']
            income_stream, _ = IncomeStream.objects.get_or_create(
                name=item['revenue_stream'],
                revenue_stream=revenue_stream)
            for transaction in transactions:
                try:
                    Transaction.objects.create(
                    date_paid=transaction['date_paid'],
                    receipt_number=transaction['receipt_number'],
                    amount=transaction['amount_paid'],
                    income_stream=income_stream
                    )
                except:
                    continue   
    return Transaction.objects.all()

def months_generator(year):
    """ Generate months in an year"""
    result = []
    today = datetime.date.today()
    current = datetime.date(year, 1, 1)
    if today.year != current.year:
        today = datetime.date(year, 12, 31)
    while current <= today:
        result.append(current.strftime('%B'))
        current += relativedelta(months=1)
    return result

def quarter_generator(year):
    """ Generate quotas in an year"""
    months = months_generator(year)
    all_quotas = ['Q1', 'Q2', 'Q3', 'Q4']
    number_of_quotas = math.ceil(len(months)/3)
    quotas = all_quotas[:number_of_quotas]
    return quotas
