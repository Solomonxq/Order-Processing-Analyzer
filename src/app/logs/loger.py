from pathlib import Path
import logging

log_path = Path("src/app/logs")
log_path.mkdir(parents=True, exist_ok=True)


logger = logging.getLogger("store_app")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(log_path / "app.log", encoding="utf-8")  


formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


logger.addHandler(console_handler)
logger.addHandler(file_handler)


