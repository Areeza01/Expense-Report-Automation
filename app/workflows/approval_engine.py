class ApprovalEngine:

    @staticmethod
    def get_approver(amount):

        if amount < 100:
            return "AUTO_APPROVED"

        if amount <= 500:
            return "MANAGER"

        return "DIRECTOR"