#!/bin/sh

nohup uvicorn main:app --host 0.0.0.0 --port 8000 > /tmp/arboreus-collector.log 2>&1 &
