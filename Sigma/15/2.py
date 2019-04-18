import requests
import json


def main():
    req = requests.get(
        'https://google.com')
    print("HTTP Status Code: " + str(req.status_code))
    print(req.headers)
    json_response = json.loads(req.content)
    print(json_response)


if __name__ == '__main__':
    main()
    # _default_decoder.decode(s)
