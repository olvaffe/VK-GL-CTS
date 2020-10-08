#!/usr/bin/python3

import sys

def parse_log(filename):
    results = {
        'Pass': 0,
        'Fail': 0,
    }
    total = 0

    category = None
    category_time = None

    look_for_time = False
    with open(filename, errors='ignore') as f:
        for line in f:
            if look_for_time:
                if line.find('The test group case duration') < 0:
                    continue

                tmp = line.split('"')
                category = tmp[1]
                s = float(tmp[-1][1:-10]) / 1000000.0
                category_time = '%.1f' % s
                break
            else:
                if not line.startswith(' <Result StatusCode'):
                    if line.startswith('#beginTestsCasesTime'):
                        look_for_time = True
                    continue

                status_code = line.split('"')[1]
                if status_code in results:
                    results[status_code] += 1
                else:
                    results[status_code] = 1
                total += 1

    print('Filename: ' + filename)
    if category:
        fields = [
            str(total),
            str(results['Pass']),
            str(results['Fail']),
            category_time,
        ]
        print('\t'.join(fields))
    else:
        print('INCOMPLETE')
    print()

for arg in sys.argv[1:]:
    parse_log(arg)

