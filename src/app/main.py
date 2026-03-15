from .core.api import OrderAPISession
from .core.utils import log_execution
from .core.validators import validate_order
from .logs.loger import logger


@log_execution
def main():
    valid_order = []

    try:
        with OrderAPISession() as api:
            orders = api.fetch_orders()

            for raw in orders:
                record = validate_order(raw)
                if record:
                    valid_order.append(record)

        logger.info(f"Валідних записів {len(valid_order)}")
        for order in valid_order:
            print(f"ID: {order.id} | Назва: {order.title} | Ціна: ${order.price:.2f}")
            print(f"Категорія: {order.category} | Рейтинг {order.rating.rate} ")
            print(f"Залишилось {order.rating.count}" )

    except Exception as e:
        logger.error(f"Помилка виконання {e}")



if __name__ == "__main__":
    main()
