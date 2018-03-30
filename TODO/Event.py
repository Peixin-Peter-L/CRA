
class Event:

    contentTuple = ("is_done", "over_due",
                    "due_date", "input_date", "due_time"
                    "priority",
                    "title", "content")

    def __init__(self, title, content, priority, due_date, due_time, is_done, over_due, input_date):
        self.title = title
        self.content = content
        self.priority = priority
        self.dueDate = due_date
        self.dueTime = due_time
        self.isDone = is_done
        self.overDue = over_due
        self.inputDate = input_date

    def change_done_status(self):
        self.isDone = not self.isDone

    def overdue(self):
        self.overDue = True

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in Event.contentTuple:
                setattr(self, key, value)

    def check_title(self):
        print(getattr(self, "title"))
