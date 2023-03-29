from datetime import datetime


def get_format_today():
    today = datetime.today()
    return today.strftime('%d %B,%Y')