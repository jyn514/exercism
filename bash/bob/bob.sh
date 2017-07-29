#!/bin/bash
input="$1"
last="${input::${#input}}"
echo "$last"
exit
