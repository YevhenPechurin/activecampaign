
from activecampaign.api.abstract_request import AbstractRequest
from activecampaign.api.consts import API_ENDPOINT


class CustomFieldsRequest(AbstractRequest):
    def __init__(self, api_request):
        super(CustomFieldsRequest, self).__init__(api_request)
        self.endpoint = API_ENDPOINT.FIELD
