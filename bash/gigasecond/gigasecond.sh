#!/usr/bin/env bash
start=$(date --date="$1" +"%s")
end="@$((start+1000000000))"
echo $(TZ='UTC' date --date="$end")

