function sayHiLater(anyFunction){
    console.log('say hi later');
    anyFunction();
}

const later = () => {
    console.log('ricky');
}


const sayHi = () => {
    console.log('sayHI er kaldt');
    later();
};

sayHiLater(sayHi);


function interact(genericMsg, name){
    console.log(genericMsg(name));
}

const genericMsg = (greetName) => {
    return `Hi ${greetName}`
}

interact((hugName) => 'hugging ' + hugName, 'eni')

interact(genericMsg, 'lars')
