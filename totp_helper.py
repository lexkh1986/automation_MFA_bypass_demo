import os
import pyotp

def get_totp_code():
    """
    Retrieves the shared secret from the environment variable 'TOTP_PINGID_KEY'
    and generates the current 6-digit TOTP token.

    Returns:
        str: The current 6-digit TOTP token.

    Raises:
        ValueError: If the environment variable 'TOTP_PINGID_KEY' is not set.
    """
    shared_secret = os.environ.get("TOTP_PINGID_KEY")
    if not shared_secret:
        raise ValueError("Environment variable 'TOTP_PINGID_KEY' is not set.")
    totp = pyotp.TOTP(shared_secret)
    return totp.now()
