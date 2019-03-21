#! /bin/bash
sudo gunicorn -D -b "0.0.0.0:6969" --access-logfile webhooks/logs/access.log --error-logfile webhooks/logs/output.log webhooks:app
