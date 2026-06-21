
# PasteDB Python SDK

Official Python SDK for [PasteDB](https://pastedb.netlify.app) — FastAPI powered text and image sharing platform.

## Installation

```
pip install pastedb
```

## Authentication

Get your API key from [PasteDB Dashboard → API Keys](https://pastedb.netlify.app/api-keys).

```bash
export PASTEDB_API_KEY="pdb_live_xxxxxxxxxxxxx"
```

## ME
● Me()
```python
from pastedb import Client


client = Client(api_key="pdb_pdb_live_xxxxxxxxxxxxx")

print(client.me())
```

Response if API key is valid

```
{
'email': 'your@email.com',
'created_at': '2026-06-21T05:26:34.361000' # Dummy
}


```

## Quick Start

```python
from pastedb import Client

# Initialize client - reads PASTEDB_API_KEY env var or pass api_key
client = Client(api_key="pdb_live_xxxxxxxxxxxxx")

# Create a paste - pass data as dict
paste = client.create_paste({
    "content": "print('Hello from PasteDB!')",
    "title": "Hello World",
    "syntax": "python"
})

print(paste["url"])  # https://pastedb.netlify.app/p/abc123
print(paste["id"])   # abc123
```

## Core API Methods

The SDK methods mirror the FastAPI backend routes. All data is passed as dictionaries and responses are returned as dictionaries.

### 1. Create Paste

`POST /pastes`

```python
from pastedb import Client
client = Client()

# Basic paste
paste = client.create_paste({
    "content": "Your text here",
    "title": "My Paste",
    "syntax": "javascript"
})

# Private paste with password
paste = client.create_paste({
    "content": "Secret data",
    "visibility": "private",
    "password": "mySecret123"
})

# Custom URL + expiry
paste = client.create_paste({
    "content": "Temporary data",
    "custom_id": "temp-data-2024",
    "expiration": "1d",
    "syntax": "json"
})
```

**Request Body**

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | str | Yes | Paste content |
| `title` | str | No | Default: `Untitled` |
| `syntax` | str | No | Default: `text` |
| `visibility` | str | No | `public` or `private`, default `public` |
| `password` | str | No | Password for private pastes |
| `custom_id` | str | No | Custom slug for URL |
| `expiration` | str | No | `1h`, `1d`, `7d`, `30d`, `never` |

**Response**

```json
{
  "id": "abc123",
  "title": "My Paste",
  "content": "Your text here",
  "syntax": "javascript",
  "visibility": "public",
  "created_at": "1781262330.906314"
}
OR
{
    'status': 'success',
    'id': '6a378ece819c1a9b62472339', 
    'custom_id': None
}



[Program finished]
```

### 2. Get Paste

`GET /pastes/{paste_id}`

```python
client = Client()

# Get by ID
paste = client.get_paste("abc123")

# Get by custom slug
paste = client.get_paste("my-custom-url")

# Get private paste - pass password in params
paste = client.get_paste("secret123", params={"password": "mySecret123"})

print(paste["title"])
print(paste["content"])
```


### 4. Update Paste

`PATCH /pastes/{paste_id}`

```python
client = Client()
paste = client.update_paste("abc123", {
    "title": "Updated Title",
    "content": "New content here",
    "syntax": "markdown"
})
```

### 5. Delete Paste

`DELETE /pastes/{paste_id}`

```python
client = Client()
client.delete_paste("abc123")
```



### 7. Get Analytics

`GET /pastes/{paste_id}/analytics`

```python
client = Client()
stats = client.get_analytics("abc123")

print(stats["views"])           # 142
print(stats["unique_visitors"]) # 89
```

## Error Handling

The SDK raises `requests.HTTPError` for API errors. Status codes match FastAPI:

```python
from pastedb import Client
from requests import HTTPError

client = Client(api_key="pdb_live_xxx")

try:
    paste = client.get_paste("invalid-id")
except HTTPError as e:
    if e.response.status_code == 404:
        print("Paste not found")
    elif e.response.status_code == 401:
        print("Invalid API key")
    elif e.response.status_code == 403:
        print("Password required")
    else:
        print(f"API error: {e}")
```

## Client Configuration

```python
from pastedb import Client

client = Client(
    api_key="pdb_live_xxx",  # Optional, uses env var if None
    base_url="https://api.pastedb.netlify.app",  # Override default   
)
```

## FastAPI Backend Reference

Your backend routes use these FastAPI dependencies:

```python
from fastapi import FastAPI, HTTPException, Depends, Query, Cookie, Request, status, Response
```

The SDK handles auth via `Authorization: Bearer <api_key>` header or cookies.

## Examples

### CLI Upload

```python
import sys
from pastedb import Client

client = Client()
content = sys.stdin.read()
paste = client.create_paste({"content": content, "title": "CLI Paste"})
print(paste["url"])
```

Usage: `cat file.py | python paste.py`



## Supported Syntax

`text`, `python`, `javascript`, `typescript`, `json`, `yaml`, `markdown`, `html`, `css`, `sql`, `bash`, `c`, `cpp`, `java`, `go`, `rust`, `php`, `ruby`, `swift`, `kotlin`, and many more.


## License

MIT License

---

Built with ❤️ using FastAPI
