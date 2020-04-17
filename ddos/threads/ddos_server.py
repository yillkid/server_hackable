#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from SocketServer import ThreadingMixIn
from  BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from time import sleep

class ThreadingServer(ThreadingMixIn, HTTPServer):
    pass

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        sleep(10)
        response = 'Slept for 10 seconds..'
        self.send_header('Content-length', len(response))
        self.end_headers()
        self.wfile.write(response)

ThreadingServer(('', 8000), RequestHandler).serve_forever()
