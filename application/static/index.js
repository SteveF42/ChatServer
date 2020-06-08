//retrieves username 
async function getUserId(){
    response = await fetch('/get_username')
    json = await response.json()
    user_name = json['user']
    return user_name
};

async function read_messages(){
    response = await fetch('/get_messages')
    obj = await response.json()
    return obj
}
async function add_messages(obj, curr_name){
    msg = obj['name'] + ": " + obj['message']

    if(curr_name === obj.name){
        $('#message-thread').append('<li class="user-message">' + msg + '</li>')
    }
    else{
        $('#message-thread').append('<li class="global-message">' + msg + '</li>')
    }
}

//connected user to socket
var socket = io.connect('http://127.0.0.1:5000/');
socket.on('connect',async function(){
    var name = await getUserId()
    socket.send({
        name : name,
        message : 'Has joined the server!'
    });
});

//button click event to send message
$('#sendButton').on('click', async function(){
    let name = await getUserId()
    var msg = $('#myMessage').val()
    $('#myMessage').val('')
    socket.send({
        name : name,
        message : msg,
    })
})

//server side event that outputs message
socket.on('message', async function(msg){
    //console.log(msg)
    var name = await getUserId()
    add_messages(msg,name)
})

window.onload = (async function(){
    messages = await read_messages()
    curr_name = await this.getUserId()
    for(var i = 0; i < messages.length-1;i++)
    {
        add_messages(messages[i],curr_name)
    }
})