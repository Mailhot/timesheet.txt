#from timesheettxt import reader, models
from timesheettxt import timesheettxt
import datetime
import helpers
import config


folder = config.data_folder
filenames = helpers.find_csv_filenames(folder)

total_result = []
total_issue_report = []
for filename in filenames:
    print(filename)
    filename_path = folder + '/' + filename

    with open(filename_path, 'r') as the_file:

        results = timesheettxt.reader.FileReader(the_file)
        issue_report = timesheettxt.report.FileReport()
        total_issue_report.append(issue_report)
        
        for result in results:
            issue_report.intervals.append(result)

        partial_result = issue_report.report_by_meta()
        total_result.append(partial_result)

total_report = {}
total_time = datetime.timedelta(0)
# print('total_result = ', total_result)
for result_dict in total_result:
    # print(result_dict)
    for result_dict_key in result_dict.keys():
        if result_dict_key in total_report.keys():
            total_report[result_dict_key]['duration'] += result_dict[result_dict_key]['duration']
        else:
            total_report[result_dict_key] = {}
            total_report[result_dict_key]['duration'] = result_dict[result_dict_key]['duration']
        # print(result_dict_key, result_dict[result_dict_key]['duration'], result_dict[result_dict_key]['billable'])
        total_time += result_dict[result_dict_key]['duration']
        
print('---------------total report----------------')
print(total_report)
key_list = list(total_report.keys())
key_list.sort()
for key in key_list:
    print(key, total_report[key]['duration'])
print(total_time)



####################################
print('')
print('intervals')
print('')
# filter
issue_filter = config.project_filter
issue_duration = datetime.timedelta(0)
total_duration = datetime.timedelta(0)
# filter for project report
for report in total_issue_report:
    # if report.
    # report = dict(report)
    for interval in report.intervals:
        if interval.meta['issue'] == issue_filter:
            # print(interval.meta['issue'], interval.description)
            print(interval)
            if interval.meta['billable']:
                issue_duration += interval.duration
            else:
                total_duration += interval.duration

print('total issue duration for %s ' %issue_filter)
print(issue_duration, 'Billable')
hours = total_duration.days * 24 + total_duration.seconds // 3600
minutes = (total_duration.seconds % 3600) // 60 /60
print('{} ({})'.format(hours + minutes, total_duration), 'Total')

print('')
print('----------------- Weekly Report for %s ------------------' %filename)

print()
print(' Total Hours: ', )

