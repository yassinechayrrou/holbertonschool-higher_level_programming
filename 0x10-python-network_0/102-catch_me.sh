#/bin/bash
# script that makes a request to server which causes a response containing specific value
curl -s -L -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
