#!/bin/bash
# Displays size of the body of the response
curl -s $1 | wc -c
