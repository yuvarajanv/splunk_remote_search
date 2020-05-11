Splunk remote query executor

This repo contains a python file 'search.py'

prerequisites python3.6

Create virtual environment(To avoid conflict between other project packages)

    1) open terminal in ubuntu
    2) run sudo apt-get install python3-tk
    3) run git clone https://github.com/yuvarajanv/splunk_remote_search.git
    2) run virtualenv -v python3.6 venv
    3) run . venv/bin/activate
    4) run pip install -r requirement.txt
    5) run python search.py

Input required:
    
    server IP address
    server PORT
    username
    password
    time range to compare: ex = 24h
    search key: ex = index="_internal" | top sourcetype

Output: 
    The output will be stored in file. The file name will be suffixed withe the current time
