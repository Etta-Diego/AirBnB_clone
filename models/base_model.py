#!/usr/bin/python3
""" A parent class that defines all common
attributes/methods for other classes"""
import uuid
from datetime import datetime

class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = created_at
