from pytube import *
import urllib.request
import json
import urllib


url_list = []
title_list = []


def search_results(text):
    global url_list
    global title_list

    temp_list = []
    videoID_list = []
    url_list = []
    x = Search(text)
    search_result_list = x.results

    for i in search_result_list:
        temp_list.append(str(i).split('=')[1])

    for elements in temp_list:
        videoID_list.append(str(elements).split(">")[0])

    for url in videoID_list:
        url_list.append('http://youtube.com/watch?v=' + url)

    for i in videoID_list:

        params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % i}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string

        with urllib.request.urlopen(url) as response:
            response_text = response.read()
            data = json.loads(response_text.decode())
            x = data['title']
            title_list.append(x)

    return title_list


print(search_results("Technoblade"))
