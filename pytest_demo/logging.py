import logging
def test_logging():
 logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='log_report.log',
    filemode='w'
)
logging.getLevelName(logging.debug)
logging.debug('This is a debug message')
logging.info('This is an informational message')
logging.warning('This is a warning message')
logging.error('This is an error message')

