class ValidationService:

    MEAL_LIMIT = 50
    HOTEL_LIMIT = 250
    EQUIPMENT_LIMIT = 500

    @staticmethod
    def validate(
        category,
        amount
    ):

        if (
            category == "Meals"
            and amount > 50
        ):
            return {
                "valid": False,
                "reason": "Meal limit exceeded"
            }

        if (
            category == "Accommodation"
            and amount > 250
        ):
            return {
                "valid": False,
                "reason": "Hotel limit exceeded"
            }

        if (
            category == "Equipment"
            and amount > 500
        ):
            return {
                "valid": False,
                "reason": "Equipment approval required"
            }

        return {
            "valid": True,
            "reason": ""
        }