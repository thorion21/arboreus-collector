import logging


def configure(logger):
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
