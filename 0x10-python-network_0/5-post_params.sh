#!/bin/bash
# Script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -X POST -F 'email=hr@holbertonschool.com' -F 'subject=I will always be here for PLD' "$1"