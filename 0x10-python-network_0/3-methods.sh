#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -I "$1" | grep Allow | awk '{print $2" "$3" "$4}'
