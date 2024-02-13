from datetime import date
class NationalPark:

    def __init__(self, name):
        self.name = name

        #self._trip =[] 
        #self._visitors = 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, 'name') and len(name)>=3: 
            self._name = name
        
    def trips(self):
        return list({trip for trip in Trip.all if trip.national_park == self})
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        total = [trip.national_park for trip in self.trips()] 
        return total.count(self)
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        if len(visitors) == 0:
            return None
        return max(visitors, key = visitors.count)


class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)


    #self.visitor._trips.append(self)
    #self.visitor._national_park.append(self.national_park)

    #self.national_park._trips.append(self)
    #self.national_park._visitors.append(self.visitors)


    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date)>=7:
            self._start_date = start_date
            # if 4<= start_date.day.value <=20:
            #     self._start_date = start_date.strftime("%B %d" + "th")
            # elif start_date.day.value[-1] == 1:
            #     self._start_date = start_date.strftime("%B %d" + "st")       
            # elif start_date.value[-1] == 2:
            #     self._start_date = start_date.strftime("%B %d" + "nd")
            # elif start_date.day.value[-1] == 3:
            #     self._start_date = start_date.strftime("%B %d" + "d")
            # else:
            #     self._start_date = start_date.strftime("%B %d" + "th")        

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date)>=7:
            self._end_date = end_date                                 






class Visitor: 

    def __init__(self, name):
        self.name = name

        #self._trips = []
        #self._national_park = []

    @property
    def name(self):
        return self._name    

    @name.setter 
    def name(self, name):
        if isinstance(name, str) and 1<= len(name) <= 15:
            self._name = name
            
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        visit = [trip.national_park for trip in self.trips() if trip.national_park == park]
        return len(visit)