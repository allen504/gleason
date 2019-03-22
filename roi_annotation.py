import random
from pathlib import Path
import cherrypy

class ROIrate(object):

    p = Path("./images")
    images = [x for x in p.iterdir()]
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
                    <img src="
                    """ + str(img) + """
                    ">
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
                </html>"""

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
                    file.write("%s, %s\n" % (key, self.rating[key]))
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
    cherrypy.quickstart(ROIrate())
