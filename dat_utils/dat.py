# Data Access Token Utils
# dat_utils.dat

# functions to help with permission checking etc

# TODO: add function to help with creating tokens too

import jwt
from datetime import datetime
from dat_utils.constants import TOKEN_MAX_LIFETIME, JWT_ALGORITHM
from dat_utils.sourceid import match_source_id_patterns


def verify_token(token, secret):
    """
    Verifies the token using the given secret, checks that it has an expiry
    time, an issued at time, and a lifetime shorter than the maximum.
    If verification is successful, returns (True, payload) where payload is the
    dict of the verified token payload. Otherwise returns (False, reason) where
    reason is a message.
    """
    try:
        payload = jwt.decode(token, secret, algorithms=[JWT_ALGORITHM])
    except (
        jwt.ExpiredSignatureError,
        jwt.InvalidIssuedAtError,
        jwt.InvalidSignatureError,
    ) as e:
        return False, "failed verification"

    # Expiry time must exist
    if not "exp" in payload:
        return False, "no expiry date"

    # Issued At time must exist
    if not "iat" in payload:
        return False, "no issued at date"

    # The length between issued at and expiry must be less than the maximum lifetime
    token_lifetime = datetime.utcfromtimestamp(
        payload["exp"]
    ) - datetime.utcfromtimestamp(payload["iat"])
    if token_lifetime > TOKEN_MAX_LIFETIME:
        return False, "lifetime too long"

    return True, payload


def check_payload_data_scope(payload, source_id, verb="read"):
    """
    Given a token and a source id, check if this token is allowed to access the source id.
    Returns True/False
    """
    if (
        not "scopes" in payload
        or not "data" in payload["scopes"]
        or not verb in payload["scopes"]["data"]
    ):
        return False

    data_scopes = payload["scopes"]["data"][verb]

    return match_source_id_patterns(source_id, data_scopes)


def verify_token_for_request(token, secret, source_id, verb="read"):
    """
    Verify the given token and check that it has permission to access the data
    source with the chosen verb.
    Returns (True, token_payload) on success, or (False, message) on failure.
    """
    result, payload = verify_token(token, secret)

    if not result:
        return False, payload
    else:
        if check_payload_data_scope(payload=payload, source_id=source_id, verb=verb):
            return True, payload
        else:
            return False, "no scope for this request"
