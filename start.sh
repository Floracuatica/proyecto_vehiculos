#!/bin/bash
gunicorn proyecto_vehiculos_django.wsgi --bind 0.0.0.0:$PORT
