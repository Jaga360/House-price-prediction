
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


function predict(){
    
    sqft= document.getElementById("sqft").value
    bhk= document.getElementById("bhk").value
    bath= document.getElementById("bath").value
    loc=document.getElementById('location').value

    details = `?sqft=${sqft}&bhk=${bhk}&bath=${bath}&loc=${loc}`

    url="/predict"+details

    fetch(url)
    .then(r => r.json())
    .then(predictedPrice => {
       div=document.getElementById('price')
       div.innerHTML=predictedPrice
    })
}