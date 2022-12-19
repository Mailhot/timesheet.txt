
from . import reader
import datetime

class FileReport:
    """docstring for FileReport"""
    def __init__(self,):
        self.intervals = []

    def report_by_meta(self,):
        results = {}
        total_time = datetime.timedelta(0)
        for interval in self.intervals:

            if interval.meta['issue'] != None:
                # check if issue already in results_billable
                if interval.meta['issue'] not in results.keys():
                    actions = []
                    actions.append(interval.description)
                    results[interval.meta['issue']] = {'duration': interval.duration, 'billable': interval.meta['billable'], 'actions': actions}
                elif interval.meta['issue'] in results.keys():
                    results[interval.meta['issue']]['duration'] += interval.duration
                    results[interval.meta['issue']]['actions'].append(interval.description)
                    # results[interval.meta['issue']] = {'duration': results[interval.meta['issue']]['duration'] + self.duration, 'billable': interval.meta['billable']}
                # print(interval.meta)
                
            elif interval.meta['issue'] == None:
                if 'None' not in results.keys():
                    actions = []
                    actions.append(interval.description)
                    results['None'] = {'duration': interval.duration, 'billable': interval.meta['billable'], 'actions': actions}
                else:
                    results['None']['duration'] += interval.duration
                    results['None']['actions'].append(interval.description)
            total_time += interval.duration

        hours, minutes, _ = convert_timedelta(total_time)
        print(f'Total: {hours}:{minutes:02d}')
        print('')

        return results

    def add_reports_by_meta(self,):
        pass


def convert_timedelta(duration):
    days, seconds = duration.days, duration.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    return hours, minutes, seconds


