import inspect
import logging


class LogGenerator:

    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("C:\\Users\\Kalpesh\\OneDrive\\Desktop\\Credence\\Notes\\Python selenium automation\\Automation site Practicing\\DrCatalystEHR\\Logs\\DrCatalystEHR.log")
        format = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger


# get log--> logging.getLogger()
# logfile --> path and name
# format --> logs format
# setFormatter -- > link file and format
# and handler --> maintenance -- >log file
