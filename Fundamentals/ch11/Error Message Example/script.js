//define sevral functions
function firstFunction() {
	secondFunction();
}
function secondFunction() {
	thirdFunction();
}
function thirdFunction() {
	fourthFunction();
}
function forthFunction() {
	headline.innerHTML = "You clicked the headline!";
}

//grab the headline element
var headline = document.getElementById("mainHeading");
//add a click event handler
headline.onclick = function() {
	firstFunction();
}