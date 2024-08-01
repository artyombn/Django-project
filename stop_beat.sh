#!/bin/bash
# stop_beat.sh
#!/bin/bash
echo "Stopping Celery Beat"

pkill -f 'celery -A Brainwave beat'
pkill -f 'celery -A Brainwave worker'

