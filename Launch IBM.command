#!/bin/zsh
# Finder launcher for the local IBM valuation workbench.

set -u

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
PREFERRED_PORT=8765
MAX_PORT=8795
SERVER_PID=""

cd "$PROJECT_DIR" || { print -u2 "ERROR: Cannot open project directory: $PROJECT_DIR"; exit 1; }

if ! command -v python3 >/dev/null 2>&1; then
  print -u2 "ERROR: python3 is required but was not found in PATH."
  exit 1
fi

if [[ ! -f app/server.py ]]; then
  print -u2 "ERROR: app/server.py was not found in $PROJECT_DIR."
  exit 1
fi

is_ibm_workbench() {
  local port="$1" response
  response="$(curl --silent --show-error --fail --max-time 2 "http://127.0.0.1:${port}/api/analysis" 2>/dev/null)" || return 1
  print -r -- "$response" | python3 -c '
import json, sys
try:
    payload = json.load(sys.stdin)
    assert "dcf" in payload and "rows" in payload and "wacc_build" in payload
except Exception:
    raise SystemExit(1)
' >/dev/null 2>&1
}

port_is_listening() {
  lsof -nP -iTCP:"$1" -sTCP:LISTEN >/dev/null 2>&1
}

pick_unused_port() {
  local candidate
  for ((candidate=PREFERRED_PORT + 1; candidate<=MAX_PORT; candidate++)); do
    if ! port_is_listening "$candidate"; then
      print -- "$candidate"
      return 0
    fi
  done
  return 1
}

wait_for_workbench() {
  local port="$1" attempt
  for ((attempt=1; attempt<=30; attempt++)); do
    if is_ibm_workbench "$port"; then
      return 0
    fi
    sleep 1
  done
  return 1
}

clear
print "IBM valuation workbench launcher"
print "Project: $PROJECT_DIR"
print ""

if is_ibm_workbench "$PREFERRED_PORT"; then
  PORT="$PREFERRED_PORT"
  REUSED=1
  print "Found a responding IBM workbench on preferred port $PORT. Reusing it."
elif port_is_listening "$PREFERRED_PORT"; then
  PORT="$(pick_unused_port)" || { print -u2 "ERROR: Ports $((PREFERRED_PORT + 1))-$MAX_PORT are occupied."; exit 1; }
  REUSED=0
  print "Port $PREFERRED_PORT is occupied by another service. Using port $PORT."
else
  PORT="$PREFERRED_PORT"
  REUSED=0
  print "Using preferred port $PORT."
fi

URL="http://127.0.0.1:${PORT}/"

if (( ! REUSED )); then
  print "Starting Python server..."
  python3 app/server.py --port "$PORT" &
  SERVER_PID=$!
  if ! wait_for_workbench "$PORT"; then
    print -u2 "ERROR: The IBM server did not respond successfully at ${URL} within 30 seconds."
    if kill -0 "$SERVER_PID" 2>/dev/null; then
      print -u2 "The server process is still running (PID $SERVER_PID). Review the messages above."
    else
      print -u2 "The server process exited during startup."
    fi
    exit 1
  fi
fi

print ""
print "IBM workbench is ready: $URL"
print "Opening the workbench in your default browser..."
open "$URL" || print -u2 "WARNING: Could not open a browser automatically. Open this URL manually: $URL"

if (( REUSED )); then
  print "Using the existing server. This Terminal window can be closed without stopping it."
  exit 0
fi

print ""
print "The server is running in this Terminal window. Keep this window open while using the workbench."
print "Press Control-C here when you are finished."
wait "$SERVER_PID"
STATUS=$?
print -u2 "IBM server stopped (exit status $STATUS)."
exit "$STATUS"
