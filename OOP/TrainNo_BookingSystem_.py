import datetime
from datetime import date

class Train:
    def book(self, TrainNo, from_station, to_station, current_date_time):
        print(f"Ticket is booked in train no:{TrainNo} from {from_station} to {to_station} on {current_date_time.strftime('%Y-%m-%d %I:%M:%S %p')}")
    def getstatus(self, TrainNo):
        print(f"Status of train no:{TrainNo}")
    def getFare(self, TrainNo, from_station, to_station):
        print(f"Fare for train no:{TrainNo} from {from_station} to {to_station}")

t = Train()
today = datetime.datetime.now() # Current date and time
t.book(1234, "Delhi", "Mumbai", today)
t.getstatus(1234)
t.getFare(1234, "Delhi", "Mumbai")