#!/bin/bash
LOGFILE="/path/to/your/logfile.log" # Replace this with the path to your log file.

while true; do
  OUTPUT=$(id user 2>&1)
  EXITCODE=$?
  echo "$(date); Exit code: ${EXITCODE}; ${OUTPUT}" >> $LOGFILE
  sleep 5
done

# nohup /path/to/your/check_id_unix_user.sh &