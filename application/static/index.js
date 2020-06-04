$(document).ready(function(){
    var name = 'test'

    var socket = io.connect('http://127.0.0.1:5000/');
    socket.on('connect',function(){
        socket.send({
            name : name + " ",
            message : 'Has joined the server!'
        });
    });

    $('#sendButton').on('click', function(){
        var msg = $('#myMessage').val()
        $('#myMessage').val('')
        socket.send({
            name : name +": ",
            message : msg,
        })
    })

    socket.on('message', function(msg){
        console.log(msg)
    })
})