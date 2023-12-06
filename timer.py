from time import time


class TimeHandler:
    def __init__(self):
        self.timer = 0
        self.start_timer()

    def start_timer(self):
        self.timer = time()

    def fetch_time(self) -> str:
        total_time = round(time() - self.timer, 2)
        return (f'{total_time} seconds  (that\'s {round(total_time / 60, 2)} minutes)'
                f'\n{self.get_exclamation(total_time)}')

    def get_exclamation(self, total_time: float):
        if total_time < 10:
            return 'That\'s pretty quick!'
        elif total_time < 60:
            return 'Not too bad!'
        elif total_time < 120:
            return 'That\'s kinda not too slow!'
        else:
            return 'Optimiziation needed....'
