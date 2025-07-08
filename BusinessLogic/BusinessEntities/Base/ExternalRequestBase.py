class ExternalRequestBase:
    """
    Base class for external requests.
    This class can be extended to create specific types of external requests.
    """

    def __init__(self, request_id: str, request_type: str):
        self.request_id = request_id
        self.request_type = request_type

    def get_request_info(self) -> dict:
        """
        Returns a dictionary containing the request information.
        """
        return {
            "request_id": self.request_id,
            "request_type": self.request_type
        }