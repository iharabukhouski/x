import pyotp

def create_otp(
    secret,
):

    totp = pyotp.TOTP(secret)

    return totp.now()

