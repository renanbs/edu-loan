from sqlalchemy import Column, DateTime

from sqlalchemy.sql import func


class TimestampedMixin(object):
    updated_at = Column(DateTime(timezone=True), default=func.now())
