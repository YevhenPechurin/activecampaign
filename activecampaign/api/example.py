from .api import Api

if __name__ == '__main__':
    token = 'c1fb70f19a1d4bf4d5f20be39bf6022ebb13a76c3de0a05bf8a13cb5c2c0ed3e09053be7'
    url = 'https://nakivo12.api-us1.com'
    api = Api(url, token)
    # response = api.contact.get_all()
    # response = api.message.get_all()
    # response = api.segment.get_all()
    response = api.custom_field_value.get_all()
    # response = api.custom_field_value.get(2)

    print(response)
