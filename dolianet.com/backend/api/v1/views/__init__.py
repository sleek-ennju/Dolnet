#!/usr/bin/env python3
"""Init file for /api/v1/views"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

if app_views:
    from api.v1.views.users import *
