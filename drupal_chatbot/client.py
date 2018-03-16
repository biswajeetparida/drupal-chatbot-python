import requests


class DrupalChatbotException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
        message = 'Error code %s: "%s"' % (code, message)
        super(DrupalChatbotException, self).__init__(message)


class DrupalChatbotClient:
    def __init__(self, api_key=None, host_url=None):
        self.api_key = api_key
        self.host_url = host_url.rstrip('/')

    def _get(self, url, args=None):
        new_args = {}
        if self.api_key:
            new_args['key'] = self.api_key
        new_args.update(args or {})
        response = requests.get(url, params=new_args)
        json_res = response.json()
        if 'error' in json_res:
            err_msg = json_res['error'].get('message')
            err_code = json_res['error'].get('code')
            raise DrupalChatbotException(message=err_msg, code=err_code)

        return json_res
