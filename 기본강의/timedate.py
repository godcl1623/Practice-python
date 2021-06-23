from datetime import datetime, timedelta
print(datetime.now().replace(hour = 9, minute=0, second=0) + timedelta(days = 100))