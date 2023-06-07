var minusButton = document.getElementById("button-minus");
var plusButton = document.getElementById("button-plus");
var quantityInput = document.getElementById("quantity-input");

minusButton.addEventListener("click", function() {
var currentValue = parseInt(quantityInput.value);
if (currentValue > 1) {
    quantityInput.value = currentValue - 1;
}
});

plusButton.addEventListener("click", function() {
var currentValue = parseInt(quantityInput.value);
if (currentValue < 10) {
    quantityInput.value = currentValue + 1;
}
});