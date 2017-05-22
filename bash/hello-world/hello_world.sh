#!/usr/bin/env bash

if [[ $@ ]] ; then
    name=$@
else
    name="World"
fi
echo "Hello, $name!"
