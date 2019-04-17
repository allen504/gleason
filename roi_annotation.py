import random
import cherrypy
import os.path
from cherrypy.lib import auth_basic

USERS = {'joe': 'allen',
         'pete': 'lawson'}

def validate_password(realm, username, password):
    if username in USERS and USERS[username] == password:
        ROIrate.user = username
        return True
    return False

class ROIrate(object):
    images = [str(x) for x in os.listdir("public/images")]
    num_images = len(images)
    r = list(range(num_images))
    random.shuffle(r)
    rating = {}
    counter = 0
    batch = 1
    if num_images <= 100:
        num_batches = 1
    else:
        num_batches = num_images // 100
    user = ""

    @cherrypy.expose
    def index(self):
            if self.counter < self.num_images:
                return self.show_img("/static/images/"+self.images[self.r[self.counter]])

    @cherrypy.expose
    def show_img(self, img):
        if self.counter % 100 == 99:
            self.batch += 1
        score = self.rating.get(self.images[self.r[self.counter]], "not yet")

        return """<html>
                  <head>
                    <link href="/static/css/style.css" rel="stylesheet">
                  </head>
                  <body>
                    <script type="text/javascript" src="/static/js/keys.js"></script>
                    <h2>Batch: {batch}/{total_batches}</h2>
                    <h2>Image: {count}/100</h2>
                    <img src={img} alt="ROI" width="512" height="512">
                    <h2>Rated: {rated}</h2>
                    <form method="get" action="score" >
                      <button id="previous" class="button" type="submit" value=b name="gleason"><-</button>
                      <button id="one" class="button" type="submit" value=1 name="gleason" onclick="score">1</button>
                      <button id="two" class="button" type="submit" value=2 name="gleason">2</button>
                      <button id="three" class="button" type="submit" value=3 name="gleason">3</button>
                      <button id="four" class="button" type="submit" value=4 name="gleason">4</button>
                      <button id="five" class="button" type="submit" value=5 name="gleason">5</button>
                      <button id="next" class="button" type="submit" value=f name="gleason">-></button>
                    </form>
                  </body>
                </html>""".format(batch = self.batch, total_batches = self.num_batches, count = self.counter+1, rated = score, img = img)

    @cherrypy.expose
    def score(self, gleason = 0):
        if gleason == "f" and self.counter < self.num_images - 1:
            self.counter += 1
            return self.index()
        elif gleason == "f" and self.counter == self.num_images - 1:
            return self.index()
        elif gleason == "b" and self.counter > 0:
            self.counter -= 1
            return self.index()
        elif gleason == "b" and self.counter == 0:
            return self.index()
        else:
            x = str(self.images[self.r[self.counter]])
            self.rating[x] = gleason
            self.write_scores(str(self.user)+"_batch_"+str(self.batch)+".csv")
            return self.index()

    @cherrypy.expose
    def write_scores(self, filename):
        with open(filename, 'w') as file:
            for key in self.rating.keys():
                file.write("%s, %s\n" % (key, self.rating[key]))
        if self.counter < self.num_images:
                return self.show_img(self.images[self.r[self.counter]])

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Set up site-wide config first so we get a log if errors occur.
    cherrypy.config.update({'server.socket_host': '127.0.0.1',
                            'server.socket_port': 80, })

    conf = {
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'public'
        },
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
            'tools.auth_basic.on': True,
            'tools.auth_basic.realm': 'localhost',
            'tools.auth_basic.checkpassword': validate_password,
            'tools.auth_basic.accept_charset': 'UTF-8',
        }
    }

    cherrypy.quickstart(ROIrate(),"/" ,config=conf)