from app.models.approval import Approval


class ApprovalRepository:

    @staticmethod
    def create(db, approval):

        db.add(approval)
        db.commit()
        db.refresh(approval)

        return approval

    @staticmethod
    def get_all(db):

        return db.query(Approval).all()