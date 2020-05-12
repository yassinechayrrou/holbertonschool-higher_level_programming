#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (err, res) {
  if (err) {
    console.error('code: 404');
  }
  console.log('code:', res && res.statusCode);
});
