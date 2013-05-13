import urllib,json

#use goagent proxies
proxies = {'http': 'http://127.0.0.1:8087'}
#fetch and print 10 pages of results
for i in xrange(1,11):
    response=urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=%s"%i,proxies=proxies)
    pyresponse=json.load(response)
    results = pyresponse["results"]
    for result in results:
        print result["text"].encode('utf-8')
