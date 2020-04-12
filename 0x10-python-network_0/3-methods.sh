#!/bin/bash
curl -I "$1" | grep "Allow" | cut -d" " -f2-
