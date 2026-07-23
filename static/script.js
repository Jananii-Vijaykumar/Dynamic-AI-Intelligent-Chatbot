async function sendMessage(){

    let input=document.getElementById("user-input");

    let message=input.value;

    if(message=="") return;

    let chat=document.getElementById("chat-box");

    chat.innerHTML += `<div class="user"><b>You:</b> ${message}</div>`;

    input.value="";

    const response=await fetch("/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })

    });

    const data=await response.json();

    chat.innerHTML += `<div class="bot"><b>Bot:</b> ${data.response}</div>`;

    chat.scrollTop=chat.scrollHeight;

}