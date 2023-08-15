class Eneba:
    """Class that represents a site which sells gift cards."""

    def __init__(self, page: int = 1, range_from: float = 0.01):
        """Constructor that initializes the class with a url and a page number."""
        self.page = page
        self.range_from = range_from
        self.url = f'https://www.eneba.com/es/store/xbox-games?drms[]=xbox&page={page}&rangeFrom={range_from}&regions[]=argentina&regions[]=emea&regions[]=global&regions[]=latam&regions[]=spain&regions[]=turkey&types[]=game'
        self.coordinates = {
            'name': {
                'type': 'span', 
                "class":'YLosEL'
            },
            'price': {
                'type': 'span', 
                "class":'L5ErLT'
            },
            'region': {
                'type': 'div', 
                "class":'Pm6lW1'
            }
        }
        
    def get_page(self) -> int:
        """Method that returns the page number."""
        return self.page
    
    def get_url(self) -> str:
        """Method that returns the url."""
        return self.url
    
    def get_range_from(self) -> float:
        """Method that returns the range_from."""
        return self.range_from
    
    def set_page(self, page: int):
        """Method that sets the page number."""
        self.page = page
        
    def set_url(self, url: str):
        """Method that sets the url."""
        self.url = url
        
    def set_range_from(self, range_from: float):
        """Method that sets the range_from."""

    def get_coordinates(self) -> dict:
        """Method that returns the coordinates."""
        return self.coordinates