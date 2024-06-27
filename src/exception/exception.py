import sys


class customexception:

    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        exc_type, exc_value, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno if exc_tb is not None else "Unknow"
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb is not None else "Unknow"
        self.error_message = error_message

    def __str__(self):
        return f"Error occurred in python script name [{self.file_name}] line number [{self.lineno}] error message [{self.error_message}]"

if __name__=="__main__":
    try:
        a = 1/0
    except Exception as e:
        raise customexception(str(e), sys)