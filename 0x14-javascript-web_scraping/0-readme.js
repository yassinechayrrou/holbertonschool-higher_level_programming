#!/usr/bin/node

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, readMe) {
  if (readMe) {
    process.stdout.write(readMe);
  }
  if (err) {
    console.error(err);
  }
});
