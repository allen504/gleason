import random
from pathlib import Path
import cherrypy
import os.path

class ROIrate(object):

    p = Path(".\images")
    images = [str(x) for x in p.iterdir()]
    for i in images:
        print(i)
    num_images = len(images)
    r = list(range(num_images))
    random.shuffle(r)
    rating = {}
    counter = 0
    @cherrypy.expose
    def index(self):
            if self.counter < self.num_images:
                return self.show_img(self.images[self.r[self.counter]])
            else:
                self.write_scores(write="1")
                return """<html>
                                <head></head>
                                <body>
                                    <p>No more images<p>
                                </body>
                          </html>"""

    @cherrypy.expose
    def show_img(self, img):
        return """<html>
                  <head></head>
                  <body>
                    <img src={img} alt="ROI" width="512" height="512">
                    <form method="get" action="score" >
                      <button type="submit" value=1 name="gleason" onclick="score">1</button>
                      <button type="submit" value=2 name="gleason">2</button>
                      <button type="submit" value=3 name="gleason">3</button>
                      <button type="submit" value=4 name="gleason">4</button>
                      <button type="submit" value=5 name="gleason">5</button>
                    </form>
                    <form method="get" action="rewind">
                        <button type="submit" value=1 name="rewind"><- Go Back</button>
                    </form>
                     <form method="get" action="write_scores">
                        <button type="submit" value=1 name="write">Save</button>
                    </form>
                  </body>
                </html>""".format(img = img)

    @cherrypy.expose
    def rewind(self, rewind = 0):
        if rewind == "1" and self.counter > 0:
            self.counter -= 1
            del self.rating[str(self.images[self.r[self.counter]])]
            return self.index()
        else:
            return self.index()

    @cherrypy.expose
    def score(self, gleason = 0):
            x = str(self.images[self.r[self.counter]])
            self.rating[x] = gleason
            self.counter += 1
            return self.index()

    @cherrypy.expose
    def write_scores(self, write = 0):
        if write == "1":
            with open('scores.csv', 'w') as file:
                for key in self.rating.keys():
                    file.write("%s, %s\n" % (key[7:], self.rating[key]))
        if self.counter < self.num_images:
                return self.show_img(self.images[self.r[self.counter]])
        else:
            return """<html>
                            <head></head>
                            <body>
                                <p>No more images<p>
                            </body>
                    </html>"""

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Set up site-wide config first so we get a log if errors occur.
    cherrypy.config.update({'server.socket_host': '127.0.0.1',
                            'server.socket_port': 80, })

    conf = {'/images': {'tools.staticdir.on': True,
                        'tools.staticdir.dir':  os.path.abspath("/images")}}
    cherrypy.quickstart(ROIrate(),"/" ,config=conf)
