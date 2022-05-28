from LoanPrediction.core.Exception.base_exception import BaseCoreException


class ColumnNotFound(BaseCoreException):
    type = "core"
    message = "Column does not exist in the csv file"
