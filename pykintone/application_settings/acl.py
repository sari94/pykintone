from pykintone.application_settings.base_administration_api import BaseAdministrationAPI
import pykintone.application_settings.setting_result as sr


class AclAPI(BaseAdministrationAPI):
    API_ROOT = "https://{0}.cybozu.com/k/v1{1}/app/acl.json"

    def __init__(self, account, api_token="", requests_options=(), app_id=""):
        super(AclAPI, self).__init__(account, api_token, requests_options, app_id)

    def _make_url(self, preview=False):
        url = self.API_ROOT.format(self.account.domain, "" if not preview else "/preview")
        return url

    def get(self, app_id="", lang="default", preview=False):
        url = self._make_url(preview)
        params = {
            "app":  app_id if app_id else self.app_id,
        }

        r = self._request("GET", url, params_or_data=params, use_api_token=False)
        return sr.GetAclResult(r)

    def update(self, _json, preview=True):
        url = self._make_url(preview)

        if isinstance(_json, dict) and "app" in _json:
            pass
        else:
            raise NotImplementedError()
        body = _json
        r = self._request("PUT", url, params_or_data=body, use_api_token=False)
        return sr.GetAclResult(r)
