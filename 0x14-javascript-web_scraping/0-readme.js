#!/usr/bin/node

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, readMe) {
  if (err != null) {
    console.log(err);
  } else {
    process.stdout.write(readMe);
  }
});
