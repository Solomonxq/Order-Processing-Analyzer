from contextlib import ContextDecorator

import requests

from ..logs.loger import logger


class OrderAPISession(ContextDecorator):
    def __enter__(self):
        logger.info("API сесія почалась")
        self.session = requests.Session()
        self.data: list[dict]
        return self

    def fetch_orders(self):
        url = "https://fakestoreapi.com/products"
        try:
            response = self.session.get(url, timeout=5)
            self.data = response.json()
            if not isinstance(self.data, list):
                logger.error("API повернув не коректні дані")

            return self.data
        except requests.RequestException:
            logger.error("API повернув не коректні дані")


    def __exit__(self, exc_type, exc_value, traceback):
        if self.session:
            self.session.close()
            logger.info("Закрив сесію")
        if exc_type:
            logger.error("Помилка при читанні")
        else:
            logger.info(f"Зчитано: {len(self.data) if self.data else 0}")

        return False


