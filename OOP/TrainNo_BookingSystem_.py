import datetime
from datetime import date

class Train:
    def __init__(self, TrainNo):
        self.TrainNo = TrainNo
        print("Train Booking System Initialized")
    def book(self, from_station, to_station, current_date_time):
        print(f"Ticket is booked in train no:{self.TrainNo} from {from_station} to {to_station} on {current_date_time.strftime('%Y-%m-%d %I:%M:%S %p')}")
    def getstatus(self):
        print(f"Status of train no:{self.TrainNo}")
    def getFare(self, from_station, to_station):
        print(f"Fare for train no:{self.TrainNo} from {from_station} to {to_station}")

t = Train(1234)  # Initialize the Train class with a train number
today = datetime.datetime.now() # Current date and time
t.book("Delhi", "Mumbai", today)
t.getstatus()
t.getFare("Delhi", "Mumbai")