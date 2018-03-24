import enum


class Priority(enum.Enum):
    NONE = "NONE"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Model(object):

    lists = {
        'Software assgnment': {'remind_me': 2, 'note': '', 'status': True, 'priority': Priority.HIGH.value},
        'Dld assgnment': {'remind_me': 2, 'note': '', 'status': False, 'priority': Priority.MEDIUM.value},
        'Web assgnment': {'remind_me': 2, 'note': '', 'status': False, 'priority': Priority.LOW.value},


    }

    def add(self, reminder, remind_me, note, priority):
        Model.lists[reminder] = {'remind_me': remind_me, 'note': note, 'status': False, 'priority': priority}

    def delete(self, reminder):
        Model.lists.pop(reminder)

    def update(self):
        pass


class View(object):
    prompt = '''
    1. list all reminders
    2. List Completed
    3. List unfinished
    4. List High Priority reminders
    5. List Medium Priority Reminders
    6. List Low Priority Reminders
    7. Create New Reminder
    8.Quit'''

    def list_prompt(self):
        print(View.prompt)

    def list_all(self, lists):
        for lis in lists:
            print(lis, ' ')

    def list_completed(self, lists):
        for lis in lists:
            if Model.lists[lis]['status']:
                print(lis, ' ')

    def list_unfinished(self, lists):
        for lis in lists:
            if not Model.lists[lis]['status']:
                print(lis, ' ')

    def list_high_priority(self, lists):
        for lis in lists:
            if Model.lists[lis]['priority'] == Priority.HIGH.value:
                print(lis, ' ')

    def list_medium_priority(self, lists):
        for lis in lists:
            if Model.lists[lis]['priority'] == Priority.MEDIUM.value:
                print(lis, ' ')

    def list_low_priority(self, lists):
        pass

    def show_new_reminder_prompt(self):
        reminder = input('reminder: ')
        remind_me = input('remind me on: ')
        note = input('note(optional): ')
        priority = input('priority(optional) (eg: HIGH, MEDIUM, LOW, NONE): ')
        return reminder, remind_me, note, priority


class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_lists(self):
        lists = self.model.lists.keys()
        return(self.view.list_all(lists))

    def get_completed(self):
        lists = self.model.lists.keys()
        return(self.view.list_completed(lists))

    def get_unfinished(self):
        lists = self.model.lists.keys()
        return(self.view.list_unfinished(lists))

    def get_high_priority(self):
        lists = self.model.lists.keys()
        return(self.view.list_high_priority(lists))

    def get_medium_priority(self):
        lists = self.model.lists.keys()
        return(self.view.list_medium_priority(lists))

    def get_low_priority(self):
        pass

    def set_reminder(self, reminder, remind_me, note="", priority=Priority.NONE.value):
        self.model.add(reminder, remind_me, note, priority)

    def start(self):
        while True:
            self.view.list_prompt()

            chooice = input("enter : ")
            if chooice is "1":
                self.get_lists()

            elif chooice == '2':
                self.get_completed()
            elif chooice == '3':
                self.get_unfinished()
            elif chooice == '4':
                self.get_high_priority()
            elif chooice == '5':
                self.get_medium_priority()
            elif chooice == '6':
                self.get_low_priority()
            elif chooice == '7':
                reminder, remind_me, note, priority = self.view.show_new_reminder_prompt()
                if reminder and remind_me and note and hasattr(Priority, priority):

                    self.set_reminder(reminder, remind_me, note, priority)

                else:
                    self.set_reminder(reminder, remind_me, note)
            elif chooice == '8':
                self.close()

            else:
                print("enter (1-8)")

    def close(self):
        quit()


class Client(object):
    controller = Controller()
    controller.start()
