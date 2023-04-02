/*!
* Start Bootstrap - Business Casual v7.0.8 (https://startbootstrap.com/theme/business-casual)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-casual/blob/master/LICENSE)
*/
// Highlights current date on contact page
window.addEventListener('DOMContentLoaded', event => {
    const listHoursArray = document.body.querySelectorAll('.list-hours li');
    listHoursArray[new Date().getDay()].classList.add(('today'));
})


let deleteModal = document.getElementById("deleteModal");
let deleteButton = document.getElementById("deleteButton");
let closeModal = document.getElementsByClassName('close-modal');

// Open the modal when how to play button clicked

deleteButton.onclick = function () {
    deleteModal.style.display = "block";
};

// Close the modal when 'x' button is clicked

closeModal.onclick = function () {
    deleteModal.style.display = "none";
};

// Modal closed when anywhere outside the modal is clicked

window.onclick = function (event) {
    if (event.target == deleteModal) {
        deleteModal.style.display = "none";
    }
};