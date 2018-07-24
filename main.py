from caesar import encrypt
import webapp2
import cgi

form="""
<form action="/" method="post">
    <label>
        Number of rotations:
        <input name ="rot" value = "%(rot)s"/></input>
    </label>
    <label>
        <br>
        <br>
        Text to encrypt:
        <textarea type = "text" name="text" value = "%(encrypt)s"/>%(answer_escaped)s</textarea>
    </label>
        <br>
        <input type="submit" value="submit"/>
</form>
"""

class Caesar(webapp2.RequestHandler):

    def write_form(self, rot = "", encrypt = "", answer_escaped = ""):
        self.response.out.write(form % {"rot": rot,
                                        "encrypt": encrypt,
                                        "answer_escaped": answer_escaped,
                                        })

    def get(self):
       self.write_form()

    def post(self):
        rot = self.request.get("rot")
        text = self.request.get("text")

        rot = int(rot)

        answer = encrypt(text, rot)
        answer_escaped = cgi.escape(answer)

        self.write_form(answer_escaped = answer_escaped)
#get returning on the page with string substitution
app = webapp2.WSGIApplication([
    ('/', Caesar)
], debug=True)
