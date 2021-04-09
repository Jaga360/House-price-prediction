


function getLocation(){

   fetch('/getLocation')
    .then(res => res.json())
    .then(data=> {
        dropdown=document.getElementById('location')
        for (loc of data) {
            dropdown.innerHTML += "<option>"+ loc + "</option>"
        }
    }) 
}