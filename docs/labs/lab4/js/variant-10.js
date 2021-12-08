function generateRandomArray() {
    return Array.from({length: 20}, () => Math.floor(Math.random() * 50)-20);
}

function getMinPositiveElement(array) {
    result = Math.max.apply(null, array);
    for (var i = 0; i < array.length; i++) {
        if ((array[i] > 0) && (result > array[i])) {
            result = array[i];
        }
    }
    return result;
}

function getMaxNegativeElement(array) {
    result = Math.min.apply(null, array);
    for (var i = 0; i < array.length; i++) {
        if ((array[i] < 0) && (result < array[i])) {
            result = array[i];
        }
    }
    return result;
}

function selectionSort(inputArr) {
    let n = inputArr.length;

    for(let i = 0; i < n; i++) {
        let min = i;
        for(let j = i; j < n; j++) {
            if(inputArr[j] < inputArr[min]) {
                min=j;
            }
        }
        if (min != i) {
            let tmp = inputArr[i];
            inputArr[i] = inputArr[min];
            inputArr[min] = tmp;
        }
    }
    return inputArr.reverse();
}

function task4v7() {
    var a = generateRandomArray();
    var ra = [...a];
    var r1 = getMaxNegativeElement(a);
    var r2 = getMinPositiveElement(a);
    var r3 = selectionSort(a);
    document.getElementById("task-4-variant-10").innerHTML = ra + "<br>"+r1+"<br>"+r2+"<br>"+r3;
}