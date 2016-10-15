var myArray = [500,500,500,500,500];

var total = 0;

for (var i = 0; i < myArray.length; i++) {
	//add the current element to the total
	total = total + myArray[i];
}

//after we are done with this loop
alert("The total is: " + total);