
# 20-m
class Course:
    def __init__(self, title, duration, teacher):
        self.title = title
        self.duration = duration
        self.teacher = teacher


class OnlineCourse(Course):
    def __init__(self, title, duration, teacher, platform, price):
        super().__init__(title, duration, teacher)
        self.platform = platform
        self.price = price

    def show_course(self):
        print(self.title, self.duration, self.teacher, self.platform, self.price)


c = OnlineCourse("Python", "3 oy", "Ali", "Udemy", 50)
c.show_course()


