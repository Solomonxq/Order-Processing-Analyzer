from .core.utils import retry, log_execution
from .core.api import OrderAPISession
from .logs.loger import logger
from .core.validators import validate_order

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
            print(f"ID: {order.id} | Назва: {order.title} | Ціна: ${order.price:.2f} | Категорія: {order.category} | Рейтинг {order.rating.rate} | Залишилось {order.rating.count}" )

    except Exception as e:
        logger.error(f"Помилка виконання {e}")



if __name__ == "__main__":
    main()