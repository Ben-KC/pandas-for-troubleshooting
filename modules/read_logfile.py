from datetime import datetime
from pathlib import Path
import re
from typing import Optional

import pandas as pd


regex = re.compile(r'^(?P<status>Starting|Finished).*(?P<time>\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d(\.\d+)?)')


def parse_to_dataframe(path: Path) -> pd.DataFrame:
    df = pd.DataFrame()
    if path.is_file():
        with path.open() as file:
            start_time: Optional[datetime] = None
            start_times = []
            calc_times = []

            for line in file:
                match = regex.match(line)

                if match is not None:
                    status = match.groupdict()['status']

                    try:
                        time = datetime.strptime(match.groupdict()['time'], '%Y-%m-%d %H:%M:%S.%f')
                    except ValueError:
                        try:
                            time = datetime.strptime(match.groupdict()['time'], '%Y-%m-%d %H:%M:%S')
                        except ValueError:
                            raise ValueError(f'Could not parse {time}')

                    if status == 'Starting':
                        start_time = time
                    else:
                        start_times.append(start_time)
                        calc_times.append((time - start_time).total_seconds())

            df = df.append(pd.DataFrame(data={'start_time': start_times, 'calc_time': calc_times}))

    return df


if __name__ == '__main__':
    import sys

    df = parse_to_dataframe(Path(sys.argv[1]))
    print(df.sample(10))
