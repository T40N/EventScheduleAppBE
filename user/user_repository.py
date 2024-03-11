from sqlalchemy.orm import Session

from shared.config.database import get_db
from user.user_model import User


class UserRepository:
    def __init__(self, db: Session = get_db()):
        self.db: Session = db

    def get_user(self, user_id: str) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self, new_user: User) -> User:
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def delete_user(self, user_id: str) -> int:
        return self.db.query(User).filter(User.id == user_id).delete()

    def get_all_users(self):
        return self.db.query(User).all()
