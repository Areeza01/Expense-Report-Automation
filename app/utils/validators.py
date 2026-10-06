def validate_amount(amount):

    if amount <= 0:
        raise ValueError(
            "Amount must be greater than 0"
        )

    return True