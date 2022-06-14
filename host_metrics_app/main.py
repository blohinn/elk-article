import datetime
import json
import os
from time import sleep

import psutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    load1, load5, load15 = psutil.getloadavg()
    ram_usage_percent = psutil.virtual_memory().percent

    log = {
        'load_avg': {
            'load1': load1,
            'load5': load5,
            'load15': load15,
        },
        'ram_usage_percent': ram_usage_percent,
        'asctime': datetime.datetime.utcnow().isoformat(timespec='milliseconds', sep=' ')
    }

    with open(os.path.join(BASE_DIR, 'host_metrics_app.log'), 'a') as f:
        f.write(json.dumps(log) + '\n')

    sleep(7)
