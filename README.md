Splunk remote query executor

This repo contains a python file 'search.py'

prerequisites python2.7, splunk-sdk==1.6.12

Input required:
    
    server IP address
    server PORT
    username
    password
    time range to compare: ex = 24h
    search key: ex = index="_internal" | top sourcetype


To run:

pip install -r requirement.txt

python search.py


Output: 
    The current output will be the list of search result.


TO DO: trigger a mail about the result in JSON format.