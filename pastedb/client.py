import requests from typing import Optional, Dict, Any, List

class PasteDBError(Exception): pass

class PasteDBClient:

def __init__(
    self,
    api_key: Optional[str] = None,
    base_url: str = "https://pastedb.onrender.com"
):

    self.base_url = base_url.rstrip("/")
    self.api_key = api_key

    self.session = requests.Session()

    if api_key:
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}"
        })

# -----------------------------
# INTERNAL
# -----------------------------

def _request(
    self,
    method: str,
    endpoint: str,
    **kwargs
):

    url = f"{self.base_url}{endpoint}"

    response = self.session.request(
        method,
        url,
        **kwargs
    )

    try:
        data = response.json()
    except Exception:
        data = response.text

    if not response.ok:
        raise PasteDBError(
            f"{response.status_code}: {data}"
        )

    return data

# -----------------------------
# PASTES
# -----------------------------

def create_paste(
    self,
    title: str,
    content: str,
    syntax: str = "plaintext",
    visibility: str = "public",
    expiration: str = "never",
    password: Optional[str] = None,
    tags: Optional[List[str]] = None
) -> Dict[str, Any]:

    payload = {
        "title": title,
        "content": content,
        "syntax": syntax,
        "visibility": visibility,
        "expiration": expiration,
        "password": password,
        "tags": tags or []
    }

    return self._request(
        "POST",
        "/paste",
        json=payload
    )

def get_paste(
    self,
    paste_id: str
) -> Dict[str, Any]:

    return self._request(
        "GET",
        f"/p/{paste_id}"
    )

def edit_paste(
    self,
    paste_id: str,
    **updates
) -> Dict[str, Any]:

    return self._request(
        "PATCH",
        f"/paste/{paste_id}",
        json=updates
    )

def delete_paste(
    self,
    paste_id: str
) -> Dict[str, Any]:

    return self._request(
        "DELETE",
        f"/paste/{paste_id}"
    )

def fork_paste(
    self,
    paste_id: str
) -> Dict[str, Any]:

    return self._request(
        "POST",
        f"/paste/{paste_id}/fork"
    )

# -----------------------------
# RAW
# -----------------------------

def raw(
    self,
    paste_id: str
) -> str:

    response = self.session.get(
        f"{self.base_url}/raw/{paste_id}"
    )

    if not response.ok:
        raise PasteDBError(response.text)

    return response.text

# -----------------------------
# SEARCH
# -----------------------------

def search(
    self,
    query: str,
    syntax: Optional[str] = None,
    user: Optional[str] = None,
    tags: Optional[List[str]] = None
) -> Dict[str, Any]:

    params = {
        "q": query
    }

    if syntax:
        params["syntax"] = syntax

    if user:
        params["user"] = user

    if tags:
        params["tags"] = ",".join(tags)

    return self._request(
        "GET",
        "/search",
        params=params
    )

def vector_search(
    self,
    query: str
) -> Dict[str, Any]:

    return self._request(
        "POST",
        "/search/vector",
        json={
            "query": query
        }
    )

# -----------------------------
# EXPLORE
# -----------------------------

def explore(self):

    return self._request(
        "GET",
        "/explore"
    )

def trending(self):

    return self._request(
        "GET",
        "/explore/trending"
    )

def latest(self):

    return self._request(
        "GET",
        "/explore/latest"
    )

def popular(self):

    return self._request(
        "GET",
        "/explore/popular"
    )

# -----------------------------
# STARS
# -----------------------------

def star(
    self,
    paste_id: str
) -> Dict[str, Any]:

    return self._request(
        "POST",
        f"/star/{paste_id}"
    )

# -----------------------------
# ANALYTICS
# -----------------------------

def paste_stats(
    self,
    paste_id: str
) -> Dict[str, Any]:

    return self._request(
        "GET",
        f"/paste/{paste_id}/stats"
    )

# -----------------------------
# USER
# -----------------------------

def me(self):

    return self._request(
        "GET",
        "/auth/me"
    )

def user_pastes(
    self,
    username: str
):

    return self._request(
        "GET",
        f"/user/{username}/pastes"
    )

def user_starred(
    self,
    username: str
):

    return self._request(
        "GET",
        f"/user/{username}/starred"
    )

# -----------------------------
# COLLECTIONS
# -----------------------------

def create_collection(
    self,
    name: str,
    description: str = ""
):

    return self._request(
        "POST",
        "/collections",
        json={
            "name": name,
            "description": description
        }
    )

def add_to_collection(
    self,
    collection_id: str,
    paste_id: str
):

    return self._request(
        "POST",
        f"/collections/{collection_id}/add",
        json={
            "paste_id": paste_id
        }
    )

def get_collection(
    self,
    collection_id: str
):

    return self._request(
        "GET",
        f"/collections/{collection_id}"
    )

# -----------------------------
# CODE RUNNER
# -----------------------------

def run(
    self,
    language: str,
    code: str
):

    return self._request(
        "POST",
        "/run",
        json={
            "language": language,
            "code": code
        }
    )

def supported_languages(self):

    return self._request(
        "GET",
        "/run/languages"
    )

# -----------------------------
# MARKDOWN
# -----------------------------

def render_markdown(
    self,
    content: str
):

    return self._request(
        "POST",
        "/markdown/render",
        json={
            "content": content
        }
    )

# -----------------------------
# API KEYS
# -----------------------------

def create_api_key(
    self,
    name: str
):

    return self._request(
        "POST",
        "/apikey/create",
        json={
            "name": name
        }
    )

def get_api_keys(self):

    return self._request(
        "GET",
        "/apikeys"
    )

def delete_api_key(
    self,
    key_id: str
):

    return self._request(
        "DELETE",
        f"/apikey/{key_id}"
    )


"""
-----------------------------

EXAMPLE

-----------------------------

if name == "main":

client = PasteDBClient(
    api_key="YOUR_API_KEY"
)

paste = client.create_paste(
    title="Hello World",
    content="print('Hello from PasteDB')",
    syntax="python"
)

print(paste)

            """
