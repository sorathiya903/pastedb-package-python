
# PasteDB Python SDK

Official Python SDK for [PasteDB](https://pastedb.netlify.app) — a fast, elegant text and image sharing platform.

## Installation

```
pip install pastedb
```

## Authentication

Get your API key from [PasteDB Dashboard → API Keys](https://pastedb.netlify.app/api-keys).

```bash
export PASTEDB_API_KEY="pdb_live_xxxxxxxxxxxxx"
```

## Quick Start

```python
from pastedb import Client

# Initialize client
client = Client(api_key="pdb_live_xxxxxxxxxxxxx")

# Create a paste
paste = client.create_paste(
    title="Hello World",
    content="print('Hello from PasteDB!')",
    syntax="python"
)

print(paste.url)  # https://pastedb.netlify.app/p/abc123
print(paste.id)   # abc123
```

## Core Features

### 1. Create Pastes

```python
from pastedb import Client
client = Client()

# Basic paste
paste = client.create_paste(
    content="Your text here",
    title="My Paste",
    syntax="javascript"
)

# Private paste with password
paste = client.create_paste(
    content="Secret data",
    visibility="private",
    password="mySecret123"
)

# Paste with custom URL and expiry
paste = client.create_paste(
    content="Temporary data",
    custom_id="temp-data-2024",
    expire_in="1d",
    syntax="json"
)

# Paste with images
paste = client.create_paste(
    content="Check out this screenshot",
    images=["/path/to/image1.png", "/path/to/image2.jpg"]
)
```

**Parameters**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `content` | str | required | The paste content |
| `title` | str | `Untitled` | Paste title |
| `syntax` | str | `text` | Syntax: `python`, `javascript`, `json`, etc |
| `visibility` | str | `public` | `public` or `private` |
| `password` | str | None | Password protect the paste |
| `custom_id` | str | None | Custom URL slug |
| `expire_in` | str | `never` | `1h`, `1d`, `7d`, `30d`, `never` |
| `images` | list | [] | Image file paths |

### 2. Get Pastes

```python
client = Client()

# Get by ID or custom slug
paste = client.get_paste("abc123")
paste = client.get_paste("my-custom-url")

print(paste.title)
print(paste.content)

# Get private paste with password
paste = client.get_paste("secret123", password="mySecret123")
```

### 3. List Your Pastes

```python
client = Client()
pastes = client.list_pastes()

for p in pastes:
    print(f"{p.title} - {p.url} - Views: {p.views}")

# Filter by visibility
public_pastes = client.list_pastes(visibility="public")

# Pagination
pastes = client.list_pastes(limit=20, offset=0)
```

### 4. Update Pastes

```python
client = Client()
paste = client.update_paste(
    "abc123",
    title="Updated Title",
    content="New content here",
    syntax="markdown"
)
```

### 5. Delete Pastes

```python
client = Client()
client.delete_paste("abc123")
```

### 6. Get Analytics

```python
client = Client()
stats = client.get_analytics("abc123")

print(stats.views)           # 142
print(stats.unique_visitors) # 89
print(stats.last_viewed)     # 2024-06-21T10:30:00Z
```

## Error Handling

```python
from pastedb import Client
from pastedb.exceptions import PasteDBError, NotFoundError, AuthError

client = Client(api_key="pdb_live_xxx")

try:
    paste = client.get_paste("invalid-id")
except NotFoundError:
    print("Paste not found")
except AuthError:
    print("Invalid API key")
except PasteDBError as e:
    print(f"API error: {e}")
```

## Advanced Usage

### Rate Limits

Free tier: 60 requests/minute  
Pro tier: 600 requests/minute

```python
client = Client(api_key="xxx", max_retries=3, timeout=30)
```

### Environment Variable

If `PASTEDB_API_KEY` is set, you can omit the key:

```python
from pastedb import Client
client = Client()  # Uses PASTEDB_API_KEY env var
```

## API Reference

### `Client(api_key=None, base_url=None, timeout=30, max_retries=3)`

Create a new PasteDB client. If `api_key` is None, reads from `PASTEDB_API_KEY` env var.

### `Paste` Object

| Attribute | Type | Description |
| --- | --- | --- |
| `id` | str | Paste ID |
| `url` | str | Full paste URL |
| `title` | str | Paste title |
| `content` | str | Paste content |
| `syntax` | str | Syntax language |
| `visibility` | str | `public` or `private` |
| `created_at` | datetime | Creation timestamp |
| `expire_at` | datetime | Expiry timestamp or None |
| `views` | int | View count |
| `images` | list | List of image URLs |

## Examples

### CLI Tool

```python
import sys
from pastedb import Client

client = Client()
content = sys.stdin.read()
paste = client.create_paste(content=content, title="CLI Paste")
print(paste.url)
```

Usage: `cat file.py | python paste.py`

## Supported Syntax Highlighting

`text`, `python`, `javascript`, `typescript`, `json`, `yaml`, `markdown`, `html`, `css`, `sql`, `bash`, `c`, `cpp`, `java`, `go`, `rust`, `php`, `ruby`, `swift`, `kotlin`, and many more.

## Security

- API keys are never logged by the SDK
- All requests use HTTPS
- Data stored on MongoDB Atlas

## Support

- **Docs**: https://pastedb.netlify.app/docs
- **Issues**: https://github.com/sorathiya903/

## License

MIT License

---

Built with ❤️ for developers by PasteDB
```
