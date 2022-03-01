__all__ = ("status_ok",)

import requests


def status_ok(url: str = "https://www.google.com", **kwargs) -> bool:
    """Test if url reachable.

    :param url: URl to test
    :type x: str
    :return: True if URL OK, False if not
    :rtype: bool
    """
    return requests.head(url, verify=False, **kwargs).ok
