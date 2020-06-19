import logging

from activecampaign.api.configuration import Configuration
from activecampaign.api.consts import USER_AGENT
from activecampaign.api.api_request import ApiRequest
from activecampaign.api.message import MessageRequest
from activecampaign.api.contact import ContactRequest
from activecampaign.api.segment import SegmentRequest
from activecampaign.api.custom_field import CustomFieldsRequest
from activecampaign.api.custom_field_value import CustomFieldValueRequest


class Api(object):
    def __init__(self, api_url, api_token):
        self._logger = logging.getLogger('activecampaign.api')
        self._api_request = ApiRequest(self._logger, Configuration(api_url, api_token), USER_AGENT)

    @property
    def message(self):
        return MessageRequest(self._api_request)

    @property
    def contact(self):
        return ContactRequest(self._api_request)

    @property
    def segment(self):
        return SegmentRequest(self._api_request)

    @property
    def custom_field(self):
        return CustomFieldsRequest(self._api_request)

    @property
    def custom_field_value(self):
        return CustomFieldValueRequest(self._api_request)

