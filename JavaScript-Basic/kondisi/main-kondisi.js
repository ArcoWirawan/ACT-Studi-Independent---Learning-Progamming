console.log()
console.log("dari file .js")

// switch case
let door = ''
switch(door) {
    case true:
        console.log("Pintu terbuka");
        document.getElementById('switch-case').innerHTML = "Pintu terbuka";  
        break;     
    case false :
        console.log("Pintu terbuka");
        document.getElementById('switch-case').innerHTML = "Pintu ditutup";
        break;
    default:
        console.log("Pintu terbuka");
        document.getElementById('switch-case').innerHTML = "Pintu rusak";


}