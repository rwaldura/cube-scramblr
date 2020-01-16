import logging

logging.basicConfig(
    format=". %(message)s",
    level=logging.DEBUG)

def print(*args) :
    strings = map(
        lambda item: str(item),
        args
    )
    logging.info(" ".join(strings))

def wait(ms) :
    return
