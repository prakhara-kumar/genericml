"""
sys : any exception which is getting controlled, this library will have that information 
err_details will be present inside sys
"""

import sys
from src.logger import logging
""" Importing from logger file in here to check if logging is working which is commented at last main one """

def error_message_detail(error, err_details:sys):

    _,_,exc_tb = err_details.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    err_message = "Error occured in python script [{0}] line number [{1}] error message [{2}]".format(

    file_name, exc_tb.tb_lineno, str(error))

    return err_message 

class CustomException(Exception):
    def __init__(self, err_message, error_details:sys):
        """ Since we are inheriting from the exception, we use super """

        super().__init__(err_message)     
        """ super().__init__(err_msg) """

        self.error_message = error_message_detail(err_message, err_details=error_details)

    """ def __str__(self) -> str: """
    def __str__(self):
        return self.error_message
        """ return super().__str__() """



""" if __name__ =='__main__':

    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e, sys) 
 """
    
    