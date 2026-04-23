import logging
from pathlib import Path


def get_logger(name):
    log_folder = Path("artifacts/latest/logs")
    log_folder.mkdir(parents=True, exist_ok=True)

    log_file = log_folder / "test_run.log"

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        console_handler = logging.StreamHandler()

        format_style = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(format_style)
        console_handler.setFormatter(format_style)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger