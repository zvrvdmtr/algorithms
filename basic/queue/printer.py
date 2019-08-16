from basic.queue.queue import Queue
import random


# Simulating printer class
# One hour, 10 students
# Every student use printer 2 times
# Student may print a paper from 1 to 20 pages
# It becomes 1 task every 180 seconds
class Printer:
    def __init__(self, ppm):
        self.current_task = None
        self.time_remaining = 0
        self.page_per_minute = ppm

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def is_busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_per_minute


class Task:

    def __init__(self, time):
        self.pages = random.randrange(1, 21)
        self.timestamp = time

    def get_time(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulation(seconds, ppm):

    lab_printer = Printer(ppm=ppm)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(seconds):

        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.is_busy()) and (not print_queue.isEmpty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))

            lab_printer.start_next(new_task=next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining."%(average_wait, print_queue.size()))


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 5)
