/*!
* Start Bootstrap - Business Casual v7.0.8 (https://startbootstrap.com/theme/business-casual)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-casual/blob/master/LICENSE)
*/
// Highlights current date on contact page
window.addEventListener('DOMContentLoaded', event => {
    const listHoursArray = document.body.querySelectorAll('.list-hours li');
    listHoursArray[new Date().getDay()].classList.add(('today'));
});


let closeModal = document.getElementById("close-modal");
const buttons = document.getElementsByClassName("open-modal");

// Gets booking info of the selected row and fills the Modal info
const buttonPressed = e => {
    let id = e.target.id;
    let name = document.getElementById("name"+id).innerHTML;
    let date = document.getElementById("date"+id).innerHTML;
    let time = document.getElementById("time"+id).innerHTML;
    let guests = document.getElementById("guests"+id).innerHTML;
    const modal = document.getElementById("deleteModal");
    const modalp = document.getElementById("modal-p");
    const keep = document.getElementById("keep-btn");


    // Open the modal when any delete button is clicked
    modal.style.display = "block";

    // Changes the Delete buttons url to delete selected booking id
    document.getElementById("delete-id").href=`/delete_booking/${id}`;

    // Close the modal when 'x' button is clicked
    closeModal.onclick = function () {
        modal.style.display = "none";
    };

    // Close the modal when 'No' button is clicked
    keep.onclick = function () {
        modal.style.display = "none";
    };

    // Modal closed when anywhere outside the modal is clicked
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };

    // Modals Paragraph is updated with the booking details of the selected row
    modalp.innerHTML = `Your booking for <strong>${name}</strong> at <strong>${time}</strong> on <strong>${date}</strong>, seating <strong>${guests}</strong> will be cancelled.`;

  };
  
  // Adds event listener to all delete buttons
  for (let button of buttons) {
    button.addEventListener("click", buttonPressed);
  }

  // Time limit for messages
  setTimeout(function() {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);
