import aiohttp

async def fetch_ical(url):
    conn = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            return await resp.read()


async def short_link(url):
    from config import U_TO_TOKEN
    endpoint = 'https://u.to/api/shorten/'
    payload = {'url': url, 'token': U_TO_TOKEN}
    headers = {'Content-Type': 'application/json'}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(endpoint, json=payload, headers=headers, ssl=False) as response:
                response.raise_for_status()
                data = await response.json()
                short_url = data.get('shortUrl')
                return short_url

    except Exception as e:
        return str(e)