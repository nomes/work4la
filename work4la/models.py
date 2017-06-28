# -*- coding: utf-8 -*-
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class ExamSubscriptionModel(Base):

    __tablename__ = 'exam_subscription'

    id = Column(Integer, primary_key=True, autoincrement=True)
    time_created = Column(DateTime)
    time_sent = Column(DateTime)
    email_address = Column(Text)
    job_id = Column(Integer)
