import os
import json
from datetime import datetime

import splunklib.client as client
import splunklib.results as results
from tkinter import Tk, Label, Entry, mainloop, Button


def init_ui():
    master = Tk()
    Label(master, text='Server IP address : ').grid(row=0)
    Label(master, text='Server PORT number : ').grid(row=1)
    Label(master, text='User Name : ').grid(row=2)
    Label(master, text='Password : ').grid(row=3)
    Label(master, text='Time Range : ').grid(row=4)
    Label(master, text='Search query : ').grid(row=5)
    ip_address = Entry(master)
    port_no = Entry(master)
    usr_name = Entry(master)
    password = Entry(master, show='*')
    time_range = Entry(master)
    search_query = Entry(master)
    ip_address.grid(row=0, column=1)
    port_no.grid(row=1, column=1)
    usr_name.grid(row=2, column=1)
    password.grid(row=3, column=1)
    time_range.grid(row=4, column=1)
    search_query.grid(row=5, column=1)

    def search():
        service = client.connect(
            host=ip_address.get(), port=int(port_no.get()),
            username=usr_name.get(), password=password.get())

        kwargs_export = {'earliest_time': '-{}'.format(time_range.get()),
                         'latest_time': 'now',
                         'search_mode': 'normal'}
        searchquery_export = 'search {}'.format(search_query.get())

        exportsearch_results = service.jobs.export(searchquery_export,
                                                   **kwargs_export)

        # Get the results and display them using the ResultsReader
        reader = results.ResultsReader(exportsearch_results)

        result_list = list()
        for result in reader:
            if isinstance(result, dict):
                result_list.append(result)
        file_name = f'search-output-{datetime.now()}.json'
        with open(file_name, "w") as outfile:
            json.dump(result_list, outfile)

        stored_path = f'Search result stored in {os.getcwd()}/{file_name}'

        child_wd = Tk()
        Label(child_wd, text=stored_path).grid(row=1)
        close_child_btn = Button(
            child_wd, text="close", command=child_wd.destroy)
        close_child_btn.grid(row=2, column=1)
        mainloop()

    search_btn = Button(master, text="Submit", command=search)
    search_btn.grid(row=6, column=0)

    close_btn = Button(master, text="close", command=master.destroy)
    close_btn.grid(row=6, column=1)
    mainloop()


init_ui()
