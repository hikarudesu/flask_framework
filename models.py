#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
from sqlalchemy.dialects.oracle.base import VARCHAR2, CHAR, DATE, NUMBER
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import Column

Base = declarative_base()

class table_1 (Base):
    __tablename__ = 'prediction_input_data'
    __table_args__ = {'schema': 'sys'}

    id = Column('id', CHAR(36), primary_key=True)
    code = Column('code', CHAR(4))
    created_at = Column('created_at', DATE)
    updated_at = Column('updated_at', DATE)

