from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UUID
from sqlalchemy.orm import relationship
from shared.config.database import Base
from shared.associations.user_event_association import event_participants


class Event(Base):
    __tablename__ = 'events'

    id = Column(UUID, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    location = Column(String)
    organizer_id = Column(UUID, ForeignKey('user.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    organizer = relationship('User', back_populates='organized_events')
    participants = relationship('User', secondary=event_participants, back_populates='participated_events')
