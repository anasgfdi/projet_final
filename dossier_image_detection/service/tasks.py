# # myapp/tasks.py

# import csv
# from .. service.models import LogEntry

# def process_log_file(file_path):
#     with open(file_path, 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             timestamp, log_level, message = row
#             LogEntry.objects.create(
#                 timestamp=timestamp,
#                 log_level=log_level,
#                 message=message
#             )
