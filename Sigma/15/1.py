import requests


def main():
    # we define a request object that is equal to requests.get('API')
    req = requests.get('https://store.steampowered.com/broadcast/ \
        ajaxgetpopularpartnerbroadcasts/?minviews=1&tagid=0&genreid=0')
    print(req.content)


if __name__ == '__main__':
    main()
