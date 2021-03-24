from manager import Manager

manager = Manager('ah', 'exective', 'test@example.com')
manager.schedule_meeting(['one@example.com', 'two@example.com', 'three@exampe.ccom'], '2021-03-24 05:15:10')
print(manager.run_next_meething())
