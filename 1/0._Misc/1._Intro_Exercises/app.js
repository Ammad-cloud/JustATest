const log = require('./logger');
const fs = require('fs');
fs.readFile('./test.txt', (err, data) => {
    if (err){
        console.log(err);
    }
    console.log(data.toString());
})

console.log('last line');
//const path = require('path');
/*const os = require('os');
var osName = os.hostname;
var totalMemory = os.totalmem/1000000; //mb
var freeMemory = os.freemem/1000000; //mb

const http = require('http');
const server = http.createServer((req, res) =>{
    if (req.url === '/'){
        res.write('hello world')
        res.end();
    }
    if(req.url ==='/api'){
        res.write(JSON.stringify([1,2,3]))
        res.end();
    }
})

server.listen(8080);
console.log('Listening on port 8080...');*/


const log1 = log.log('Hej');
console.log(log1);
const log2 = log.log2('Hej igen');
console.log(log2);