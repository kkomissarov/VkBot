import datetime


georgian_date = datetime.date(2018, 6, 4)
now_date = georgian_date.today()
days_count = georgian_date.toordinal() - now_date.toordinal()



