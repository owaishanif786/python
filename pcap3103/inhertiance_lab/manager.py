from employee import Employee
import collections
class Manager(Employee):
    def __init__(self, name, title, email_address, phone_number=''):
        super().__init__(name, title, email_address, phone_number=phone_number)
        #  self.invitees = invitees
        #  self.time = time
        self.meetings = {}
        # self.meetings = []

    def schedule_meeting(self, invitees, time):
        meeting = {time: invitees}
        self.meetings[time] = invitees
        self.meetings = collections.OrderedDict(sorted(self.meetings.items()))
        # self.meetings.sort(key=lambda m:m['time'])
    
    def run_next_meething(self):
        return self.meetings.popitem()
    
