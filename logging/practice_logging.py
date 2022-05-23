import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

# basicConfig : Default log level is WARNING = 30
logging.basicConfig(filename="./logs",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode="w") # append by default "a"

logger = logging.getLogger()
# logger.debug("Our first message")
# logger.info("Our first message")
# logger.warning("Our first message")
# logger.error("Our first message")
# logger.critical("Our first message")
# print(logger.level)

def division(a,b)->float:
    """ Return the division of two numbers """
    logger.debug(f"division of {a}/{b}")
    try:
        result = a/b
        logger.debug(f"the result is {result}")
        return result
    except Exception as e:
        logger.error(e)
        return e

print(division(15,5))
print(division(15,0))
