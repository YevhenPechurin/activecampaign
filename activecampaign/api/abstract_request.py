
class AbstractRequest(object):
    def __init__(self, api_request):
        self._api_request = api_request
        self.endpoint = ''

    def create(self):
        return self._api_request.post_request(endpoint=self.endpoint)

    def get_all(self):
        return self._api_request.get_request(endpoint=self.endpoint)

    def get(self, object_id):
        return self._api_request.get_request(endpoint=self.endpoint + '/' + str(object_id))

    def update(self, object_id, json_data=None):
        return self._api_request.put_request(
            endpoint=self.endpoint + '/' + str(object_id), json_data=json_data)

    def delete(self, object_id):
        return self._api_request.delete_request(endpoint=self.endpoint + '/' + str(object_id))