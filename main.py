#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        html = urllib2.urlopen("http://www.vpngate.net/cn/").read()
        ips = re.findall(r"<td class='vg_table_row_1'><b><span style='font-size: 12pt;'>(.+?)</span></b></td><td class='vg_table_row_1' style='text-align: right;'><b><span style='font-size: 10pt;'>(.+?)</span></b><BR><span style='font-size: 9pt;'>(.+?)</span><BR>(.+?)<b>L2TP/IPsec<BR>连接指南</b>", html)
        if ips:
            self.response.write(ips[0][0])
        else:
            self.response.write("No L2TP IP")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
