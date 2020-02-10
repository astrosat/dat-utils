# dat_utils.jwt

# Utilities for JWT

import re

# JWT's base64 encoding does NOT include padding '=' at the end
BEARER_REGEX = re.compile("Bearer ([A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+)")


def get_bearer_token(auth_header_value):
    """
    Given the value of the Authentication header, extract the token.
    Returns the token if it contains one, otherwise None.
    """
    m = BEARER_REGEX.match(auth_header_value)

    if m is None:
        return None
    else:
        return m.group(1)
