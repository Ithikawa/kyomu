#!/usr/bin/env python
from __future__ import print_function

import os
import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

import middlecore

class MyHandler(PatternMatchingEventHandler):
    def __init__(self):
        super(MyHandler, self).__init__(patterns="*.jpg")

    def on_created(self, event):
        middlecore.main(event._src_path,"rest.txt","comic_list.txt")

def watch():
    path = os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\AppData\\Local\\Packages\\Microsoft.YourPhone_8wekyb3d8bbwe\\LocalCache\\Indexed\\3BD89B5F-A29C-4690-9145-71D563396433\\User\\Pixel 3\\最近の写真"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    print("start program")
    watch()