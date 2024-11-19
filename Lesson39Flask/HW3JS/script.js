
// for (i=0; i < allInputs.length; i++ ) {
//     allInputs[i].addEventListener("focus", () => {
//         //search for the lable related to this input
//         const lable = document.querySelector();
//         lable.style.fontWeight = "bold";
        
//     })
// }

const addNameLable = document.getElementById("fullNameLable");
const nameInput = document.getElementById("fullname");

nameInput.addEventListener("focus", ()=> {
    
    addNameLable.style.fontWeight = "bold";
})

nameInput.addEventListener("blur", ()=> {
    addNameLable.style.fontWeight = "normal";
    nameInput.style.color="green"
})



