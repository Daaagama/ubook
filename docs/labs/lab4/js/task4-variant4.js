var arrA = [5, 2, 1, 1, 2, 1, 1, 5, 1, 1];
var arrB = [2, 1, 3, 1, 3, 1, 2, 1, 1, 4];
var arrC = [];

function guardarNumerosA(element) {
 	boxvalue = document.getElementById(element).value;
 	arrA = boxvalue.split(", ", 10).map(Number);
 	if (!checkSize(arrA)) {
 		arrA = [];
 	}
}

function guardarNumerosB(element) {
 	boxvalue = document.getElementById(element).value;
 	arrB = boxvalue.split(", ", 10).map(Number);
 	if (!checkSize(arrB)) {
 		arrB = [];
 	}
}

function checkSize(arr) {
 	if (arr.length < 10) {
 		alert("Введений масив повинен мати 10 символів");
 		return false;
 	}
 	return true;
}

function calculateC() {

 	guardarNumerosA("ArrayA")
 	guardarNumerosB("ArrayB")
 	document.getElementById("arrayA").innerHTML = arrA.join(", ");
 	document.getElementById("arrayB").innerHTML = arrB.join(", ");
 	arrC = calcC();
 	document.getElementById("arrayC1").innerHTML = arrC.map(round).join(", ");
 	arrC = changeElements(arrC);
 	document.getElementById("arrayC2").innerHTML = arrC.map(round).join(", ");
 	arrC = bubbleSort(arrC);
 	document.getElementById("arrayC3").innerHTML = arrC.map(round).join(", ");
}

function calcC() {
	var c = []
 	for (var i = 0; i < 10; i++) {
  		if (arrA[i] == arrB[i]) {
  			c[i] = 1;
  		} else {
  			c[i] = (1 / (arrA[i] - arrB[i]));
  		}
	}
	return c
}

function changeElements(arr) {
 	 var arr_first = arr[0]
 	arr[0] = arr[9];
 	arr[9] = arr_first;
 	return arr
}

function bubbleSort(arr){
	for(var i = 0; i < arr.length; i++){
		for(var j = 0; j < ( arr.length - i -1 ); j++){
			if(arr[j] > arr[j+1]){
				var temp = arr[j]
				arr[j] = arr[j + 1]
				arr[j+1] = temp
			}
		}
	}
	return arr
}


function round(element){
	return element.toFixed(2);
}