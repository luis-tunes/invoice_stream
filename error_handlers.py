import logging

def handle_vision_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            logging.error("""For more info on error messages, check: 
                          https://cloud.google.com/apis/design/errors""")
            raise
    return wrapper