#!/bin/sh
celery -A crawler worker --loglevel=info
