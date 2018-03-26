import MonthFrame
from Clock import *


class IndependentMonthFrame(MonthFrame.MonthFrame):
    def __init__(self, master=None):
        # Pass a different font size for showing purpose
        super().__init__(month=Clock.get_instance().currentMonth, master=master, font_size=17)

    # Different title
    def place_content(self):
        super().place_content()
        self.monthTitle.config(text=str(Clock.monthTuple[self.showingMonth - 1]) + " " + str(self.showingYear))

    # Different title
    def update_graphics(self):
        super().update_graphics()
        self.monthTitle.config(text=str(Clock.monthTuple[self.showingMonth - 1]) + " " + str(self.showingYear))

    # Need to consider days of next and previous month
    def update_bind_action_days(self):
        for weekNum in range(len(self.days)):
            for day in self.days[weekNum]:
                # Previous Month
                if weekNum < 2 and int(day.cget("text")) > 14:
                    # If it is January
                    if self.showingMonth == 1:
                        day.bind("<Button-1>", lambda event, d=day.cget("text"), m=12,
                                 y=self.showingYear-1: self.dayCallback(d, m, y))
                    else:
                        day.bind("<Button-1>", lambda event, d=day.cget("text"), m=self.showingMonth-1,
                                 y=self.showingYear: self.dayCallback(d, m, y))
                # Next month
                elif weekNum > 3 and int(day.cget("text")) < 21:
                    # If it is December
                    if self.showingMonth == 12:
                        day.bind("<Button-1>", lambda event, d=day.cget("text"), m=1,
                                 y=self.showingYear+1: self.dayCallback(d, m, y))
                    else:
                        day.bind("<Button-1>", lambda event, d=day.cget("text"), m=self.showingMonth+1,
                                 y=self.showingYear: self.dayCallback(d, m, y))

