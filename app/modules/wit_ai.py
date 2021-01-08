import os
from wit import Wit


def get_wit_analysis(text: str) -> dict:
    """
    Sends the provided text string to Wit.ai for Intent and Entity analysis.
    :param text: String to be analyzed by Wit.ai.
    :return: Dictionary containing Wit.ai's analysis.
    """
    access_token = os.getenv("WIT_ACCESS_TOKEN", "NO WIT ACCESS TOKEN FOUND")
    client = Wit(access_token)
    response = client.message(text)
    return response
