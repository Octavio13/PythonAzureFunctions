import requests

class HttpService:

    def __init__(self) -> None:
        pass

    def send_request(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            # Request was successful, process the response
            data = response.json()
            return data
        else:
            # Request failed, handle the error
            return f'Error:, {response.status_code}'


    def __validate_resopnse():
        pass
