from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import logging

# create logger with 'spam_application'
logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('server.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s [%(levelname)s] - [%(name)s]%(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

PORT_NUMBER = 8080

#this class will handle any incoming request from the browser
class myHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET(self):
		if self.path=="/":
			self.path="/index.html"
			logging.info("[GET][%s] - %s", self.headers['Host'], self.path)
		try:
			#check the file extension required and set mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype = 'text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype = 'image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/json'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path)
				self.send_response(200)
				self.send_header('Content-type', mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return

		except IOError:
			self.send_error(404, 'File Not Found: %s' % self.path)

try:
	#create a web server and define the handler to manage the incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER

	#Wait forever for incoming http requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
