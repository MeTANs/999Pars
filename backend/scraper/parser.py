import aiohttp 
from aiohttp import ClientSession, ClientResponse

class BaseScraper:
    
    def __init__(self, url: str, headers: dict, query: dict):
        self.url = url
        self.headers = headers
        self.query = query

    async def get_request(self) -> ClientResponse:
        
        async with ClientSession() as session:
            async with session.get(self.url, 
                                   headers=self.headers,
                                   json=self.query) as response:
                return await response.text()
    

class Car(BaseScraper):
    
   async def scrap_car(html):
       