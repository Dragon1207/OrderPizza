fetch('/contextdata')
.then(response => response.json())
.then(data => {document.getElementById("orders_count").innerHTML=data.orders_count});
