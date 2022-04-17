from flask import Flask, render_template 
import random 
app = Flask(__name__) 
#list of cat images 
images = [
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr05/15/9/anigif _enhanced-buzz-26388-1381844103-11.gif",
    "http://ak-hdl.buzzfed.com/static/2013-16/enhanced/webdr01/15/9/anigi f_enhanced—buzz-31540-1381844535-8.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26390-1381844163-18.gif",
    "http://ak-hdl.buzzfed.com/static/2013-16/enhanced/webdr06/15/10/anigif _enhanced~buz2-1376-1381846217-8.gif",
    "http://ak-hdl.buzzfed.com/static/2013-168/enhanced/webdr03/15/9/anigif_enhanced—buzz-3391-1381844336-26.gif",
    "http://ak-hdl.buzzfed.com/static/2013-16/enhanced/webdr06/15/10/anigif_enhanced-buzz-29111-1381845968-8.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr03/15/9/anigif_enhanced-buzz-3469-1381844582-13.gif",
    "http://ak-hdl.buzzfed.com/static/2013-10/enhanced/webdr82/15/9/anigif_enhanced—buzz-19667-1381844937-168.gif",
    "http://ak-hdl.buzzfed.coa/static/2013-16/enhanced/webdr05/15/9/anigif_enhanced—buzz-26358-1381845043-13.gif",
    "http://ak-hdl.buzzfed.com/static/2013-16/enhanced/webdr06/15/9/anigif_enhanced—buzz-18774-1381844645-6.gif",
    "http://ak-hdl.buzzfed.com/static/2613-10/enhanced/webdr06/15/9/anigif_enhanced-buzz-25158-1381844793-0.gif",
    "http://ak-hdl.buzzfed.com/static/2013-18/enhanced/webdr03/15/10/anigif_enhanced-buz2z-11980-1381846269-1.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template(‘index.html’, url=url)
if __name__ == "__main__":
    app.run(host="0.0.0.0")
