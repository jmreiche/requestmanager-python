class ResponseBase:
    """
    Base class for all response entities.
    This class can be extended to create specific response types.
    """
    
    def __init__(self, success: bool = True, message: str = ""):
        self.success = success
        self.message = message

    def to_dict(self):
        """
        Convert the response to a dictionary format.
        """
        return {
            "success": self.success,
            "message": self.message
        }