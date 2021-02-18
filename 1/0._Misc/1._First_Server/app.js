const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send({message: "this is my homepage"});
});

app.get('/users', (req, res) => {
    const users = [{
        user1: "Carl", hobby: 'Coding',
        user2: "Henning", hobby: 'Coding',
        user3: "Laura", hobby: 'Coding'
    }];
    res.send(users);
})

app.get('/users/create', (req, res) => {
    console.log('Create user here:  ');
})

app.post('/users/create', (req, res) => {
    console.log('got into POST request');
})

app.put('/users/update/:id', (req, res) => {
    const id = req.params.id;
    console.log('got into PUT request by ', id);
})

app.delete('/users/delele/:id', (req, res) => {
    const id = req.params.id;
    console.log('got into DELETE request by ', id);
})

app.listen(8080);
