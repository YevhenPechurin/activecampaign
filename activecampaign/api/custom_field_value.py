
from activecampaign.api.abstract_request import AbstractRequest
from activecampaign.api.consts import API_ENDPOINT


class CustomFieldValueRequest(AbstractRequest):
    def __init__(self, api_request):
        super(CustomFieldValueRequest, self).__init__(api_request)
        self.endpoint = API_ENDPOINT.FIELD_VALUE
