import aiohttp 
from aiohttp import ClientSession, ClientResponse
from bs4 import BeautifulSoup

class BaseScraper:
    
    def __init__(self, url: str, headers: dict, query: dict):
        self.url = url
        self.headers = headers
        self.query = query

    async def fetch_html(self) -> ClientResponse:
        
        async with ClientSession() as session:
            async with session.get(self.url, 
                                   headers=self.headers,
                                   json=self.query) as response:
                return await response.text()
    
    async def get_navbar(self):
        html = await self.fetch_html(self.url)
        soup = BeautifulSoup(html, "lxml")
        
        
    

class CarScraper(BaseScraper):
    
   async def scrap_car(html):
       