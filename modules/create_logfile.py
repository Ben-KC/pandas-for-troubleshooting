from datetime import datetime, timedelta
from pathlib import Path
from random import random, uniform


dates = [
    datetime(year=2021, month=1, day=1),
    datetime(year=2021, month=2, day=11),
    datetime(year=2021, month=3, day=5),
    datetime(year=2021, month=3, day=20),
    datetime(year=2021, month=4, day=13),
    datetime(year=2021, month=4, day=22),
    datetime(year=2021, month=5, day=6),
]

times = [2.2, 12.3, 11.0, 10.5, 9.3, 8.7, 8.1]


def create_logfile(path: Path):
    with path.open('w') as file:
        current_time = dates[0]
        for x in range(len(dates) - 1):
            end_time = dates[x+1]
            calc_time = times[x]

            while current_time < end_time:
                actual_calc_time = uniform((0.75*calc_time), (1.25*calc_time))

                file.write(f'Starting calculation at {current_time}\n')
                file.write('Doing something...\n')
                file.write('Doing something...\n')
                file.write('Doing something...\n')

                current_time = current_time + timedelta(seconds=actual_calc_time)

                file.write(f'Finished calculation at {current_time}\n')

                current_time = current_time + timedelta(seconds=random())


if __name__ == '__main__':
    import sys

    print('Creating logfile...')
    create_logfile(Path(sys.argv[1]))
    print('Done!')
