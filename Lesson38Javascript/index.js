console.log("Hello World from web");
//randomly replace the background of body red blue
let colors = ["red", "blue"];
let randomColor = colors[Math.floor(Math.random() * colors.length)];
document.body.style.backgroundColor = randomColor;


// Write function to get two arguments your name and age and should print to console “My name” + name + “, and my age:” + age.
// Call that function with your name and age
// Rewrite function to be arrow function.
// Call the second function.
function printNameAndAge(name, age) {
    console.log(`My name ${name}, and my age: ${age}`);
}

printNameAndAge("John", 25);

const printNameAndAgeArrow = (name, age) => {
    console.log("Ma name: " + name + ", and my age: " + age);
}

printNameAndAgeArrow("Ned", 30);

// ARRAYS
const fruits = ["apple", "banana", "orange"];
//push lemon to the end of the array
fruits.push("lemon");
console.log(fruits);

console.log(fruits.toString())

console.log(fruits.sort().reverse());


// document.body.children[3].children[0].children[0].style.border = "5px solid black";
const changeContent = (newContent) => {
    var nodes = document.querySelectorAll("p.intro");
    console.log(nodes);
    nodes.forEach(node => {
        node.innerHTML = "<button>newContent</button> <br> <p>newContent</p> <br> <h1>newContent</h1>";
    });
}


const hideParagraphs = () => {
    var nodes = document.querySelectorAll("p.intro");
    console.log(nodes);
    nodes.forEach(node => {
        node.style.display = "none";
    });
}

const showParagraphs = () => {
    var nodes = document.querySelectorAll("p.intro");
    console.log(nodes);
    nodes.forEach(node => {
        node.style.display = "block";
    });
}


// change the image to john snow
// 1. select the element and save in the variable
// 2. change the src attribute of the element
const changeToJohn = () => {
    const arja = document.getElementById("myimg")
    arja.src = "HW2CSS/john.png";   
}


// add event listener to the image Arja which will change the image to john snow
const arja = document.getElementById("myimg");
arja.addEventListener("click", changeToJohn);


// add event listener to the same image which on mouse over will 
// change the image back to arja
arja.addEventListener("mouseleave", () => {
    arja.src = "HW2CSS/arja.png";
});
















