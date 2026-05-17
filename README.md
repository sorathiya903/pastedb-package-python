# PasteDB Python SDK

Official Python SDK for interacting with the PasteDB API.

Supports:

- Create and manage pastes
- Explore public pastes
- Semantic vector search
- Star system
- Collections
- Markdown rendering
- Code execution
- API key management
- Analytics

---

# Installation

```

pip install pastedb

```


---

Quick Start

```
import pastedb

client = PasteDBClient(
    api_key="YOUR_API_KEY"
)

paste = client.create_paste(
    title="Hello World",
    content="print('Hello')",
    syntax="python"
)

print(paste)
```
---

Initialize Client
```
from client import PasteDBClient

client = PasteDBClient(
    api_key="YOUR_API_KEY"
)
```
Parameters

Parameter| Type| Description
api_key| str| Your PasteDB API key
base_url| str| Custom API URL

---

Paste Methods
```
create_paste()
```
Create a new paste.
```
paste = client.create_paste(
    title="Example",
    content="print('Hello')",
    syntax="python"
)
```
Parameters

Parameter| Type| Default| Description
title| str| Required| Paste title
content| str| Required| Paste content
syntax| str| plaintext| Syntax language
visibility| str| public| public/private/unlisted
expiration| str| never| Expiration time
password| str| None| Password protection
tags| list| []| Tags list

---
```
get_paste()
```
Get a paste by ID.
```
paste = client.get_paste("abc123")
```
---
```
edit_paste()
```
Edit an existing paste.
```
client.edit_paste(
    "abc123",
    title="Updated Title"
)
```
You can update:

- title
- content
- syntax
- visibility
- tags
- expiration

---
```
delete_paste()
```
Delete a paste.
```
client.delete_paste("abc123")
```
---
```
fork_paste()
```
Create a copy of an existing paste.
```
forked = client.fork_paste("abc123")
```
---
```
raw()
```
Get raw paste text.
```
raw = client.raw("abc123")

print(raw)
```
---

## Search Methods
```
search()
```
Search public pastes.
```
results = client.search(
    query="fastapi auth",
    syntax="python"
)
```
Parameters

Parameter| Type| Description
query| str| Search query
syntax| str| Filter by language
user| str| Filter by user
tags| list| Filter by tags

---
```
vector_search()
```
Semantic vector search powered by MongoDB Vector Search.
```
results = client.vector_search(
    "dark animated navbar"
)
```
Finds similar pastes by meaning instead of exact keywords.

---

## Explore Methods
```
explore()
```
Get explore page pastes.
```
pastes = client.explore()
```
---
```
trending()
```
Get trending pastes.
```
trending = client.trending()
```
---
```
latest()
```
Get latest public pastes.
```
latest = client.latest()
```
---
```
popular()
```
Get most popular pastes.

popular = client.popular()

---

## Star Methods
```
star()
```
Toggle star on a paste.
```
client.star("abc123")
```
If already starred, it removes the star.

---

## Analytics Methods
```
paste_stats()
```
Get analytics for a paste.
```
stats = client.paste_stats("abc123")
```
Example response:
```
{
    "views": 120,
    "copies": 30,
    "shares": 12,
    "stars": 9
}
```
---

## User Methods
```
me()
```
Get current authenticated user.
```
user = client.me()
```
---
```
user_pastes()
```
Get public pastes from a user.
```
pastes = client.user_pastes("aditya")
```
---
```
user_starred()
```
Get starred pastes from a user.
```
starred = client.user_starred("aditya")
```
---

## Collection Methods
```
create_collection()
```
Create a collection.
```
collection = client.create_collection(
    name="Frontend Snippets",
    description="Useful frontend snippets"
)
```
---
```
add_to_collection()
```
Add paste to collection.
```
client.add_to_collection(
    collection_id="123",
    paste_id="abc123"
)
```
---
```
get_collection()
```
Get collection details.
```
collection = client.get_collection("123")
```
---

## Code Runner Methods
```
run()
```
Execute code.
```
result = client.run(
    language="python",
    code="print('Hello')"
)
```
---
```
supported_languages()
```
Get supported execution languages.
```
languages = client.supported_languages()
```
---

## Markdown Methods
```
render_markdown()
```
Render markdown into HTML.
```
html = client.render_markdown(
    "# Hello World"
)
```
---

## API Key Methods
```
create_api_key()
```
Create API key.
```
key = client.create_api_key(
    "My Application"
)
```
---
```
get_api_keys()
```
Get all API keys.
```
keys = client.get_api_keys()
```
---
```
delete_api_key()
```
Delete API key.
```
client.delete_api_key("key123")
```
---

Error Handling

The SDK raises "PasteDBError" when requests fail.
```
from client import PasteDBClient, PasteDBError

try:

    client = PasteDBClient(
        api_key="INVALID"
    )

    client.me()

except PasteDBError as e:

    print(e)
```
---

Example Project
```
from client import PasteDBClient

client = PasteDBClient(
    api_key="YOUR_API_KEY"
)

paste = client.create_paste(
    title="Quick Sort",
    content="print('Sorting')",
    syntax="python",
    tags=["algorithm", "python"]
)

print("Created:", paste)

stats = client.paste_stats(
    paste["id"]
)

print(stats)
```
---

Features

- Clean Python API
- Easy authentication
- Semantic search
- Code execution
- Collections support
- Markdown rendering
- Analytics support
- API key management
- Fast integration

---

License

MIT License
