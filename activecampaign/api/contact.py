from activecampaign.api.consts import API_ENDPOINT
from activecampaign.api.custom_field import CustomField
from activecampaign.api.custom_field_value import CustomFieldValue


class Attribute:
    def __init__(self, model, name):
        self.model = model
        self.name = name


class Contact(object):
    def __init__(self, id=None, cdate=None, email=None,
                 phone=None, first_name=None,
                 last_name=None):
        self.id = id
        self.cdate = cdate
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name
        self._custom_fields = {}
        self._custom_fields_value = {}

    def from_dict(self, data):
        if 'cdate' in data:
            self.cdate = data['cdate']
        if 'email' in data:
            self.email = data['email']
        if 'phone' in data:
            self.phone = data['phone']
        if 'firstName' in data:
            self.first_name = data['firstName']
        if 'lastName' in data:
            self.last_name = data['lastName']
        return self

    def to_dict(self):
        data = {
            'cdate': self.cdate,
            'email': self.email,
            'phone': self.phone,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }
        return data

    def __getattr__(self, name):
        if self.id:
            return self._get_field_value(name)
        else:
            raise AttributeError(name)

    def _get_field_value(self, name):
        field = self.custom_fields_value.get(name, None)
        if field is None:
            field = CustomFieldValue(self, name)
            self._custom_fields_value[name] = field
        return field

    def _get_field(self, name):
        field = self.custom_fields.get(name, None)
        if field is None:
            field_id = CustomField(self, name)
            self._custom_fields[name] = field_id
        return field


class Contacts(object):
    def __init__(self, meta_data=None):
        self.contacts = []
        self.meta_data = meta_data

    def from_dict(self, data):
        if 'meta' in data:
            self.meta_data = data['meta']
        if 'contacts' in data and isinstance(data['contacts'], list):
            for contact_data in data['contacts']:
                self.contacts.append(Contact().from_dict(contact_data))
        return self


class ContactRequest(object):
    def __init__(self, api_request):
        self._api_request = api_request

    def create(self):
        return self._api_request.post_request(endpoint=API_ENDPOINT.CONTACT)

    def create_or_update(self, params):
        return self._api_request.post_request(
            endpoint=API_ENDPOINT.CONTACT + '/sync',
            params=params)

    def lists(self, params):
        return self._api_request.post_request(
            endpoint=API_ENDPOINT.CONTACT + '/contactLists',
            payload=params)

    def automations(self, message_id):
        return self._api_request.post_request(
            endpoint=API_ENDPOINT.CONTACT + '/' + message_id + '/contactAutomations')

    def get_all_to_object(self, params=None):
        if not params:
            params = {"status": "-1", "orders[email]": "ASC"}
        return Contacts().from_dict(self._api_request.get_request(
            endpoint=API_ENDPOINT.CONTACT,
            params=params))

    def get_all(self, params=None):
        if not params:
            params = {"status": "-1", "orders[email]": "ASC"}
        return self._api_request.get_request(
            endpoint=API_ENDPOINT.CONTACT,
            params=params)

    def get(self, message_id):
        return self._api_request.get_request(endpoint=API_ENDPOINT.CONTACT + '/' + message_id)

    def update(self, message_id):
        return self._api_request.put_request(endpoint=API_ENDPOINT.CONTACT + '/' + message_id)

    def delete(self, message_id):
        return self._api_request.delete_request(endpoint=API_ENDPOINT.CONTACT + '/' + message_id)
