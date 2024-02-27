class Train():
    def __init__(self, name, fare,seatNo, tSeats):
        self.name=name
        self.fare=fare
        self.seatNo=seatNo
        self.tSeats=tSeats
        self.tSeats=[]
        for i in range(1,tSeats+1):
            self.tSeats.append(i)
        print("Seats which still need to be reserved are:\n", self.tSeats)

    def getStatus(self):
        print(f"Number of seats left in the train are {len(self.tSeats)}")
        
    def fareInfo(self):
        print(f"The fare of the train is Rs. {self.fare}.")

    def bookTicket(self, seatNo):
        self.seatNo=seatNo
        print(f"The name of the train is {self.name}.")
        if seatNo not in self.tSeats:
            print(f"Kindly enter valid seat number.")
            print("Seats which still need to be reserved are:\n", self.tSeats)
        elif seatNo in self.tSeats:
            print(f"Your ticket has been booked. Your seat number is {self.seatNo}")
            self.tSeats.remove(self.seatNo)
            print("Seats which still need to be reserved are:\n", self.tSeats)
        else:
            print("Sorry! This train is full. Kindly try reserving the ticket of next train.")
    def cancelSeat(self, seatNo):
        self.seatNo=seatNo
        self.tSeats.append(seatNo)
        print(f"Seat number {seatNo} has been cancelled.")
        print("Seats which still need to be reserved are:\n", self.tSeats)

pakrail=Train("Pakistan Railways", 200, 20, 300)
pakrail.getStatus()
pakrail.bookTicket(219)
pakrail.getStatus()
pakrail.bookTicket(218)
pakrail.getStatus()
pakrail.cancelSeat(219)
pakrail.getStatus()