from sqlalchemy import Column, Integer, String, DateTime, UUID, func
from sqlalchemy.orm import relationship
from shared.config.database import Base
from shared.associations.user_event_association import event_participants


class User(Base):
    __tablename__ = 'user'

    id = Column(UUID, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String)
    surname = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    participated_events = relationship('Event', secondary=event_participants, back_populates='participants')
    organized_events = relationship('Event', back_populates='organizer')
    access_level = Column(Integer)
