from sqlalchemy import Column, DateTime

from sqlalchemy.sql import func


class TimestampedMixin(object):
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
