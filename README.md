Data Access Token Utils
=======================

Modules:

 * `dat_utils.dat`: Functions for verifying a data access token
 * `dat_utils.jwt`: Function helpers for JWTs
 * `dat_utils.sourcid`: Functions for manipulating Source IDs

Example usage:

```python3
# Validate the token with the secret key, issue time and expiration, and check scope permission

is_valid, payload = verify_token_for_request(
                        token=token,
                        secret_key=SECRET_KEY,
                        source_id='astrosat/forestry/canopy-change/2019-12-07',
                        verb='read'
                    )

if is_valid:
    print("Token valid", payload)

else:
    err_message = payload
    print("Token not valid", err_message)

```
