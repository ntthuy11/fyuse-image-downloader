import urllib2

imgurl_pattern = "https://i.fyu.se/kqysvi4w01v7f0ou/7naymp0llj/frames_{}.jpg"
imgsave_pattern = "{:04}.jpg"

i = 0
while True:
    try:
        img = urllib2.urlopen(imgurl_pattern.format(i))
        f = open(imgsave_pattern.format(i), 'wb')
        f.write(img.read())
        f.close()
        i += 1
    except urllib2.URLError as e:
        if i > 0:
            print "Done!"
        else:
            print e.reason
        break