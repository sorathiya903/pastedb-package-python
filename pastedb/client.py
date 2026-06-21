import requests
from typing import Optional, Dict, Any, List


class PasteDBError(Exception):
    pass


class Client:

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://pastedb-rw62.onrender.com"
    ):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key

        self.session = requests.Session()

        if api_key:
            self.session.headers.update({
                "x-api-key": api_key,
                "Authorization": f"Bearer {api_key}"
            })

    # -------------------------
    # INTERNAL REQUEST HANDLER
    # -------------------------
    def _request(self, method: str, endpoint: str, **kwargs):

        url = f"{self.base_url}{endpoint}"

        res = self.session.request(method, url, timeout=30, **kwargs)

        try:
            data = res.json()
        except Exception:
            data = res.text

        if not res.ok:
            raise PasteDBError(f"{res.status_code}: {data}")

        return data

    # =========================
    # AUTH / USER
    # =========================
    def me(self):
        return self._request("GET", "/api/me")

    # =========================
    # PASTE CORE (PUBLIC API)
    # =========================
    def create_paste(self, data: Dict[str, Any]):
        return self._request("POST", "/create", json=data)

    def get_paste(self, paste_id: str):
        return self._request("GET", f"/p/{paste_id}")

    
    def api_update_paste(  self,  paste_id: str,   data: Dict[str, Any]):
        return self._request(
            "PUT",
            f"/api/paste/{paste_id}",
            json=data
        )
    # =========================
    # SEARCH / EXPLORE
    # =========================
    
    def explore(self):
        return self._request("GET", "/explore")

    # =========================
    # EXTRA FEATURES
    # =========================
    
    def run_code(self, language: str, code: str):
        return self._request(
            "POST",
            "/run",
            json={"language": language, "code": code}
        )

    def get_images(self, paste_id: str):
        return self._request("GET", f"/images/{paste_id}")

    def paste_stats(self, paste_id: str):
        return self._request("GET", f"/stats/{paste_id}")

    def check_custom_id(self, custom_id: str):
        return self._request("GET", "/check-id", params={"id": custom_id})

    # =========================
    # API KEY SYSTEM
    # =========================
    def generate_api_key(self, name: str):
        return self._request("POST", "/generate-api-key", json={"name": name})

    def my_api_keys(self):
        return self._request("GET", "/my-api-keys")

    def delete_api_key(self, api_key: str):
        return self._request("DELETE", f"/delete-api-key/{api_key}")

    # =========================
    # API VERSION (x-api-key auth)
    # =========================
    def api_me(self):
        return self._request("GET", "/api/me")

    def api_create_paste(self, data: Dict[str, Any]):
        return self._request("POST", "/api/create", json=data)

    def api_get_paste(self, paste_id: str):
        return self._request("GET", f"/api/paste/{paste_id}")

    def api_delete_paste(self, paste_id: str):
        return self._request("DELETE", f"/api/paste/{paste_id}")

    def api_update_paste(self, paste_id: str, data: Dict[str, Any]):
        return self._request("PUT", f"/api/paste/{paste_id}", json=data)

    def api_user_pastes(self):
        return self._request("GET", "/api/pastes")
