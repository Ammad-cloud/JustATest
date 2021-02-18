let url = 'http://mylogger.io/log'

function log(message){
    console.log(`Log 1 er nu kaldt: ${message}`);
}

function log2(message){
    console.log(`Log 2 er nu kaldt: ${message}`);
}


module.exports = {
    log, log2
}