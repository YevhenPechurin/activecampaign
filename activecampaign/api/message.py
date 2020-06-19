from activecampaign.api.consts import API_ENDPOINT


class MessageRequest(object):
    def __init__(self, api_request):
        self._api_request = api_request

    def create(self):
        return self._api_request.post_request(endpoint=API_ENDPOINT.MESSAGE)

    def get_all(self):
        return self._api_request.get_request(endpoint=API_ENDPOINT.MESSAGE)

    def get(self, message_id):
        return self._api_request.get_request(endpoint=API_ENDPOINT.MESSAGE + '/' + message_id)

    def update(self, message_id):
        return self._api_request.put_request(endpoint=API_ENDPOINT.MESSAGE + '/' + message_id)

    def delete(self, message_id):
        return self._api_request.delete_request(endpoint=API_ENDPOINT.MESSAGE + '/' + message_id)
