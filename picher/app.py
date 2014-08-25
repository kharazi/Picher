import urllib2
from flask import Flask


app = Flask(__name__)

@app.route('/<string:feed>')
def main(feed):
	url = "http://feeds.feedburner.com/%s" % feed
	# url = "http://www.asriran.com/%s" % feed
	url = url.replace('0', '/')
	feed = urllib2.urlopen(url).read()
	return feed


if __name__ == '__main__':
    app.run(debug=True)
