# import logging
#
# class LogGen:
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename=".\\Logs\\automation.log",
#                             format='%(asctime)s : %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',)
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger


import os
import logging

class LogGen:
    @staticmethod
    def loggen():
        log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../Logs")
        if not os.path.exists(log_path):
            os.makedirs(log_path)

        logger = logging.getLogger("nopCommerce")
        if not logger.handlers:  # Only add handler once
            file_handler = logging.FileHandler(os.path.join(log_path, "automation.log"), mode="a")
            formatter = logging.Formatter("%(asctime)s : %(levelname)s - %(message)s", "%m/%d/%Y %I:%M:%S %p")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.setLevel(logging.INFO)

        print("Logger configured with file:", os.path.join(log_path, "automation.log"))
        return logger
