var http = require("http");

http.createServer(function (request, response) {
  // send the HTTP header
  // HTTP status: 200 OK
  // Content Type: text/plain
  response.writeHead(200, {'Content-Type': 'text/plain'});

  // send response as hello world
  response.end('Hello World\n');
}).listen(8081);

var fs = require("fs");

var data = fs.readFileSync('input.txt');

console.log(data.toString());
