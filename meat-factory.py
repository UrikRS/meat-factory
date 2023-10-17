from time import localtime, strftime, sleep
from threading import Thread, Lock
import random


lock = Lock()


def now():
    return strftime("%Y-%m-%d %H:%M:%S", localtime())


def take_meat(worker):
    with lock:
        global meats
        if meats:
            meat = random.choice(meats)
            meats.remove(meat)
            print(f'{worker} 在 {now()} 取得{meat}')
            return meat
        else:
            return None


def meat_processing(worker, meat):
    while meat:
        match meat:
            case '牛肉':
                sleep(1)
            case '豬肉':
                sleep(2)
            case '雞肉':
                sleep(3)
        print(f'{worker} 在 {now()} 處理完{meat}')
        meat = take_meat(worker)


class Worker:
    def __init__(self, name) -> None:
        self.name = name
        self.work = Thread(
            target=meat_processing,
            args=(self.name, take_meat(self.name)),
        )


if __name__ == '__main__':
    meats = ['牛肉'] * 10 + ['豬肉'] * 7 + ['雞肉'] * 5
    worker_names = ['A', 'B', 'C', 'D', 'E']
    workers = [Worker(name) for name in worker_names]

    for worker in workers:
        worker.work.start()
