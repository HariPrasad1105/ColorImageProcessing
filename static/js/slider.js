
// Update the current slider value (each time you drag the slider handle)
function onSliderUpdate(inputValue, inputID) {
    document.getElementById(inputID).value = inputValue
}

function updateSlider(sliderValue, inputID) {
    console.log(inputID);
    document.getElementById(inputID).value = sliderValue;
}