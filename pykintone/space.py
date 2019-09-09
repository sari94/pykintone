from pykintone.base_api import BaseAPI
import pykintone.model_result as mr


class Space(BaseAPI):
    API_ROOT = "https://{0}.cybozu.com/k/v1/{1}"

    def __init__(self, account, api_token="", requests_options=()):
        super(Space, self).__init__(account, api_token, requests_options)

    def __space(self):
        return self.API_ROOT.format(self.account.domain, "space.json")

    def __template_space(self):
        return self.API_ROOT.format(self.account.domain, "template/space.json")

    def __space_body(self):
        return self.API_ROOT.format(self.account.domain, "space/body.json")

    def __space_thread(self):
        return self.API_ROOT.format(self.account.domain, "space/thread.json")

    def __space_members(self):
        return self.API_ROOT.format(self.account.domain, "space/members.json")

    def get(self, space_id):
        url = self.__space()
        params = {"id": space_id}
        resp = self._request("GET", url, params_or_data=params)
        r = mr.RawResult(resp)
        return r

    def delete(self, space_id):
        url = self.__space()
        params = {"id": space_id}
        resp = self._request("DELETE", url, params_or_data=params)
        r = mr.RawResult(resp)
        return r

    def create(self, data):
        url = self.__template_space()
        resp = self._request("POST", url, params_or_data=data)
        r = mr.RawResult(resp)
        return r

    def update_body(self, data):
        url = self.__space_body()
        resp = self._request("PUT", url, params_or_data=data)
        r = mr.RawResult(resp)
        return r

    def update_thread(self, data):
        url = self.__space_thread()
        resp = self._request("PUT", url, params_or_data=data)
        r = mr.RawResult(resp)
        return r

    def get_members(self, space_id):
        url = self.__space_members()
        params = {"id": space_id}
        resp = self._request("GET", url, params_or_data=params)
        r = mr.RawResult(resp)
        return r
