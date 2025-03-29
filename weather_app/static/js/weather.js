function temp_convert(temp, button) {
    let temperature_celsius = temp;
    console.log('button_click: ', button.dataset.clicked);
    if (button.dataset.clicked === "true") {
        let temperature_fahrenheit = ((temperature_celsius * 9 / 5) + 32).toFixed(2);
        button.textContent = '℉';
        button.dataset.clicked = "false";
        button.closest('.city-container').querySelector('.temperature-color').textContent = temperature_fahrenheit;
    } else {
        button.textContent = '℃';
        button.dataset.clicked = "true";
        button.closest('.city-container').querySelector('.temperature-color').textContent = temp;
    }
}
