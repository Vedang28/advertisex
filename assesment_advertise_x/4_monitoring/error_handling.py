import logging

logging.basicConfig(level=logging.ERROR)

def log_error(error_message):
    logging.error(error_message)

# Example usage
try:
    # Some processing logic
    pass
except Exception as e:
    log_error(str(e))
