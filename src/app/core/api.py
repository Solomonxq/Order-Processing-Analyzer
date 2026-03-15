import requests
from contextlib import ContextDecorator
from .exepcions import OrderFetchError

class OrderAPISession(ContextDecorator):
    def __enter__(self):
        print("API session started")
        self.session = requests.Session()
        url = "https://fakestoreapi.com/products"
        try:
            response = self.session.get(url, timeout=5)
            data = response.json()
            if not isinstance(data, list):
                raise OrderFetchError("API повернув некоректні дані")
            return data  
        except requests.RequestException as e:
            raise OrderFetchError(f"Не вдалося отримати дані з API: {e}")

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
        print("API session closed")
        return False 

# Використання
with OrderAPISession() as orders:
    print(orders)  