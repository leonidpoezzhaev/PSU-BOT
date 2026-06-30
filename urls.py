import aiohttp

async def fetch_ical(url: str) -> bytes:
    conn = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            return await resp.read()

async def fetch_url(session, endpoint, url):
    params = {'url': url}
    async with session.get(endpoint, params=params) as response:
        return await response.text()


async def short_link(url):
    endpoint = 'https://clck.ru/--'

    async with aiohttp.ClientSession() as session:
        response_text = await fetch_url(session, endpoint, url)
        return response_text