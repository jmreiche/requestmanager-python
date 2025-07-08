class ExternalResponseBase:
    """
    Base class for external responses.
    This class is intended to be extended to create specific types of external responses.
    """

    def __init__(self, response_id: str, status: str):
        """
        Initializes a new instance of the ExternalResponseBase class.

        :param response_id: Unique identifier for the response.
        :param status: Status of the response (e.g., "success", "error").
        """
        self.response_id = response_id
        self.status = status

    def get_response_info(self) -> dict:
        """
        Returns a dictionary containing the response information.

        :return: A dictionary with response_id and status.
        """
        return {
            "response_id": self.response_id,
            "status": self.status
        }