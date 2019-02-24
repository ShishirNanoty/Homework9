class Vehicle():
    def __init__(self,make = 'NA',model = 'NA',year = 1900,weight =0, maint = False,trips = 0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.maint = maint
        self.trips = trips
        

    def setMake(self, make):
        self.make = make
    def setModel(self, model):
        self.model = model
    def setYear(self, year):
        self.year = year
    def setWeight(self, weight):
        self.weight = weight

    def __str__(self):
        return 'Make>>' + self.make +"\n" + 'Model>>' + self.model + "\n" + 'Year>>' + str(self.year) +"\n"+ 'Weight>>' + str(self. weight) + '\n' + 'Maint status>>' + str(self.maint) + '\n' + 'Trips since maint>>' + str(self.trips) + '\n'

class Cars(Vehicle):
    def __init__(self,make,model,year,weight, maint = False,trips = 0):
        Vehicle.__init__(self,make,model,year,weight, maint,trips)
        self.isDriving = False

    def Drive(self):
        self.isDriving = True
    def Stop(self):
        self.isDriving = False
        self.trips += 60
        if self.trips >= 100:
            self.maint = True
    def Repair(self):
        self.maint = False
        self.trips = 0


v1 = Cars('Tata', 'Indica', 2010, 1000)
v2 = Cars('BMW', 'XB001', 2017, 1500)
v3 = Cars('Ford', 'KL200', 1995, 1300)
print('Initial state for Car1:\n', v1)
print('Initial state for Car2:\n', v2)
print('Initial state for Car3:\n', v3)
v1.Drive()
v1.Stop()
v1.Drive()
v1.Stop()
# print('Final State for Car1:\n',v1)
v2.Drive()
v2.Stop()
# print('Final State Car2:\n',v2)
v1.Drive()
v2.Drive()
v1.Stop()
v2.Stop()
print('State for Car1:\n',v1)
print('State for Car2:\n',v2)
v1.Repair()
v2.Repair()
print('Final State after maintenance Car1:\n',v1)
print('Final State after maintenance Car2:\n',v2)
