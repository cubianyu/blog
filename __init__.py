#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Inotify tools for entries
version 1.0
history:
2013-6-19    dylanninin@gmail.com    init
"""

from config import blogconfig as config
from service import EntryService

entryService = EntryService()

import os
import threading
from qiniu import Auth, BucketManager

class EntryMonitor:
    def __init__(self):
        self._lock = threading.RLock()
        self._stop_cond = threading.Condition(self._lock)
        self._stop = False

        self.qiniu = Auth(config.qiniu_ak, config.qiniu_sk)
        self.blog_bucket = BucketManager(self.qiniu)
        self.blog_prefix = "raw/"

        self._thread = threading.Thread(target = self.run, name="blog_entry_monitor")
        self._thread.daemon = True
        self._thread.start()

    def __del__(self):
        with self._lock:
            self._stop = True
            self._stop_cond.notify()
        self._thread.join()

    def run(self):
        with self._lock:
            while not self._stop:
                try:
                    local_list = {}
                    for root, _, files in os.walk(config.entry_dir):
                        for f in files:
                            local_list[f] = False

                    ret, _, info = self.blog_bucket.list(config.qiniu_bucket, prefix = "raw/")
                    file_list = eval(info.text_body)["items"]
                    print "find file list %s" % file_list
                    for f in file_list:
                        if f["key"].startswith(self.blog_prefix) and f["mimeType"] == "text/markdown":
                            file_name = f["key"][len(self.blog_prefix):]
                            if file_name not in local_list:
                                entryService.download_file(file_name, f["key"])
                                entryService.add_entry(True, 'raw/entry/' + file_name)
                            else:
                                local_list[file_name] = True

                    for f in local_list.keys():
                        if not local_list[f]:
                            print "remove entry %s" % f
                            entryService.delete_entry(os.path.abspath('raw/entry/' + f))
                            os.remove('raw/entry/' + f)
                except Exception, e:
                    print "***************** %s *****************" % e
                self._stop_cond.wait(10)

entryMonitor = EntryMonitor()
