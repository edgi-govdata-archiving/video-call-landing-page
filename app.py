from flask import Flask, request, render_template, jsonify
from flaskext.markdown import Markdown
import json
import re
import requests
import urllib
from scrapy.selector import Selector

app = Flask(__name__)
Markdown(app)

@app.route('/')
def help():
    return render_template('help.html')

@app.route('/<path:url>')
def process(url):
    # Reconstitute url querystrings that flask got greedy with
    querystrings = urllib.parse.urlencode(request.args)
    url = url + '?' + querystrings
    template_kwargs = {'call_url': url}
    if 'zoom.us' in url:
        m = re.match('.*zoom.us/j/(\d+).*', url)
        mid = m.group(1)
        # See: https://stackoverflow.com/a/23439106
        mid = ' '.join([mid[i:i+3] for i in range(0, len(mid), 3)])
        template_kwargs.update({'meeting_id': mid})
    return render_template('landing-page.html', **template_kwargs)

def get_data(url):
    r = requests.get(url)
    sel = Selector(r)
    if sel.xpath('//meta[@property="og:type"]/@content').extract_first() != 'events.event':
        return {}

    data = {
            'url': sel.xpath('//link[@rel="canonical"]/@href').extract_first(),
            'title': sel.xpath('//meta[@property="og:title"]/@content').extract_first(),
            'description': sel.xpath('//meta[@property="og:description"]/@content').extract_first(),
            'start_time': sel.xpath('//meta[@property="event:start_time"]/@content').extract_first(),
            'end_time': sel.xpath('//meta[@property="event:end_time"]/@content').extract_first(),
            'location': sel.xpath('//meta[@name="twitter:data1"]/@value').extract_first(),
            }

    return data

