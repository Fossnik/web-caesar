import webapp2
import caesar

class MainHandler(webapp2.RequestHandler):
	def get(self):
		message = 'Hello World'
		encrypted_message = caesar.encrypt(message, 13)
		self.response.write(encrypted_message)

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
