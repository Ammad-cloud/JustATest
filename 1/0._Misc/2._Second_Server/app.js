const express = require('express');
const app = express();
//const app = require('express')();

app.get("/", (req, res) =>{
    res.send({});
});

app.get("/welcome", (req, res) =>{
    res.send("<h1>Welcome</>")
});

app.get("/me", (req, res) =>{
    res.send({
        "name" : "Ammad",
        "age" : 12
    });
});

app.listen(8080);