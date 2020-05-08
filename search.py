import logging
import json

import splunklib.client as client
import splunklib.results as results
logger = logging.getLogger(__name__)

HOST = raw_input('enter server IP address : ')
PORT = int(raw_input('enter server PORT : '))
USERNAME = raw_input('enter user name : ')
PASSWORD = raw_input('enter password : ')
earliest_time = raw_input('time range : ')
search_key = raw_input('enter search query : ')

service = client.connect(
    host=HOST, port=PORT, username=USERNAME, password=PASSWORD)

kwargs_export = {'earliest_time': '-{}'.format(earliest_time),
                 'latest_time': 'now',
                 'search_mode': 'normal'}
searchquery_export = 'search {}'.format(search_key)

exportsearch_results = service.jobs.export(searchquery_export, **kwargs_export)

# Get the results and display them using the ResultsReader
reader = results.ResultsReader(exportsearch_results)

result_list = list()
for result in reader:
    if isinstance(result, dict):
        result_list.append(result)

print json.dumps(result_list)

#To do: send mail
