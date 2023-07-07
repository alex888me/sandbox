#!/bin/bash
LOGFILE="/path/to/your/logfile.log" # Replace this with the path to your log file.

while true; do
  TIMEFORMAT="%R " # Setting time format and preventing newline
  OUTPUT=$( { time id user; } 2>&1) # Running the command and storing the output.
  EXITCODE=$? # Storing the exit code of the last run command.
  echo -n "$(date): " >> $LOGFILE
  echo -n "${OUTPUT}, " >> $LOGFILE
  echo "Exit code: ${EXITCODE}" >> $LOGFILE
  sleep 5
done

# nohup /path/to/your/check_id_unix_user.sh &