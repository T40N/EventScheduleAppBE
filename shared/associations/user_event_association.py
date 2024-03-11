from sqlalchemy import Table, Column, Integer, ForeignKey
from shared.config.database import Base
from typing import ForwardRef

event_participants = Table('event_participants', Base.metadata,
                           Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
                           Column('event_id', Integer, ForeignKey('event.id'), primary_key=True)
                           )
