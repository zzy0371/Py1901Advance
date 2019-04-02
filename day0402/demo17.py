# 1导入logging模块
import logging
# logging.Formatter

logging.basicConfig(level=logging.DEBUG, filename='sys.log',format='%(asctime)s-%(message)s-%(lineno)d-%(levelname)s')

logging.error("中国")
logging.info("info:789")
logging.warning("warn:999")