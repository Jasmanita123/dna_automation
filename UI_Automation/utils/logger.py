import logging
import os


def get_logger(name):
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(f"{log_folder}/automation.log")
        console_handler = logging.StreamHandler()

        format_style = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler.setFormatter(format_style)
        console_handler.setFormatter(format_style)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger