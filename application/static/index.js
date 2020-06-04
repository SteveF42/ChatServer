
//retrieves username 
async function getUserId(){
    response = await fetch('/get_username')
    json = await response.json()
    user_name = json['user']
    return user_name
};



//connected user to socket
var socket = io.connect('http://127.0.0.1:5000/');
socket.on('connect',async function(){
    var name = await getUserId()
    socket.send({
        name : name + " ",
        message : 'Has joined the server!'
    });
});

//button click event to send message
$('#sendButton').on('click', async function(){
    let name = await getUserId()
    var msg = $('#myMessage').val()
    $('#myMessage').val('')
    socket.send({
        name : name +": ",
        message : msg,
    })
})

//server side event that outputs message
socket.on('message', function(msg){
    console.log(msg)
    $('#message-thread').append('<li>' + msg + '</li>')
})
