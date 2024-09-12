let array = [];

function addElement() {
    let value = prompt("Enter value to add:");
    array.push(value);
    renderArray();
}

function removeElement() {
    array.pop();
    renderArray();
}

function renderArray() {
    const container = document.getElementById('array-visualization');
    container.innerHTML = ''; // Clear the previous visualization

    array.forEach((element, index) => {
        const elemDiv = document.createElement('div');
        elemDiv.className = 'array-element';
        elemDiv.innerHTML = element;
        container.appendChild(elemDiv);
    });
}
