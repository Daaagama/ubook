// // let block = document.querySelector('.content');
//
// function checkNumber(AStr) {
//     AStr = AStr.replace(/[\s\-]/g, '');
//     return AStr.match(/^((\+?3)?8)?((0\(\d{2}\)?)|(\(0\d{2}\))|(0\d{2}))\d{7}$/) != null;
// }
//
// // checkNumber(input.value)
// function showCheck(AStr) {
//     console.log(checkNumber(AStr));
//     // checkNumber(AStr) ? block.innerHTML = 'Вірно введений код' : block.innerHTML = 'Невірно введений код'
//     if (checkNumber(AStr)) console.log('wwww');
// }
//
// let input = document.querySelectorAll('input[name="phone"]');
// // let btn = document.querySelector('input[type="submit"]');
//
// input.forEach(item => {
//     item.onkeyup = function (e) {
//         if (e.target.value.length > 13) console.log('value > 13')
//         this.value = this.value.replace(/[^\d]/g, '');
//         showCheck(e.target.value);
//     }
// })

let inputs = document.querySelectorAll('input[name="phone"]');
let btn = document.querySelector('input[type="submit"]');
//
let im = new Inputmask('0(99)999-99-99');

inputs.forEach(el => im.mask(el))