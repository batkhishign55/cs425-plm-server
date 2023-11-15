class UINotif {
  constructor() {}
}

var myModal = new bootstrap.Modal(document.getElementById('myModal'), {
  keyboard: false
})

function showModal(message) {
  var modalBody = document.getElementById("modalBody");
  modalBody.innerHTML = message;
  myModal.show();
}