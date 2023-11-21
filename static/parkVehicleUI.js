window.addEventListener("load", function () {
  new ApiPark().callApiLots().then(new UIPark().showLots);
});

let lotList = [];
let selectedLot;

class ApiPark {
  async callApiLots() {
    return await fetch("/lot/api/all")
      .then(async (res) => {
        if (res.status === 200) {
          const jsonresp = await res.json();
          jsonrespsave = jsonresp.data;
          return jsonresp;
        } else {
          const jsonresp = await res.json();
          showModal(res.status + " " + jsonresp.message);
        }
      })
      .catch((e) => {
        showModal(e);
      });
  }
}

class UIPark {
  constructor() {
    this.showLots = this.showLots.bind(this);
  }

  loadPage(page) {
    let dropdown = document.getElementById("lotListId2");
    dropdown.innerHTML = page;
  }

  showLots(apiresp) {
    let lotRows = [];
    for (let lot of apiresp.data) {
      let row = this.createRow(lot);
      lotRows.push(row);
    }

    this.loadPage(lotRows.join(""));

    fetch("/vehicle/api/")
      .then(async (res) => {
        if (res.status === 200) {
          const jsonresp = await res.json();
          let vehicletRows = [];

          for (const vehicle of jsonresp.data) {
            vehicletRows.push(
              `<option value="${vehicle[0]}">${vehicle[2]}</option>`
            );
          }
          let dropdown = document.getElementById("vehicleId");
          dropdown.innerHTML = vehicletRows.join("");
        } else {
          const jsonresp = await res.json();
          showModal(jsonresp.message);
        }
      })
      .catch((e) => {
        showModal(e);
      });
  }

  createRow(lot) {
    const cardTemplate = `
        <li><a class="dropdown-item" href="#" onclick="itemPressed(${lot[0]})">${lot[0]}, ${lot[1]}, ${lot[2]}, ${lot[5]}</a></li>`;
    return cardTemplate;
  }
}

$(document).ready(function () {
  $("#parkingLot").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    let dropdown = document.getElementById("lotListId2");
    if (value == "" || value == null) {
      $(dropdown).removeClass("show");
    } else {
      $(dropdown).addClass("show");
    }

    $("#lotListId2 li").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
});

function setParkingSpot() {
  fetch("/lot/api/spot?" + new URLSearchParams({ lotId: selected }))
    .then(async (res) => {
      if (res.status === 200) {
        const jsonresp = await res.json();
        let spotRows = [];

        for (const spot of jsonresp.data) {
          spotRows.push(`<option value="${spot[0]}">${spot[0]}</option>`);
        }
        let dropdown = document.getElementById("spotId");
        dropdown.innerHTML = spotRows.join("");
      } else if (res.status === 404) {
        let dropdown = document.getElementById("spotId");
        dropdown.innerHTML = "";
      } else {
        const jsonresp = await res.json();
        showModal(jsonresp.message);
      }
    })
    .catch((e) => {
      showModal(e);
    });
}

function itemPressed(lotId) {
  selected = lotId;
  let dropdown = document.getElementById("lotListId2");
  $(dropdown).removeClass("show");

  const res = jsonrespsave.filter((lot) => lot[0] === lotId)[0];
  document.getElementById(
    "parkingLot"
  ).value = `${res[0]}, ${res[1]}, ${res[2]}, ${res[5]}`;
  setParkingSpot();
}

document
  .getElementById("form2")
  .addEventListener("submit", async function (evt) {
    // evt.preventDefault();
    const elements = document.getElementById("form2").elements;

    const obj = {};
    for (const element of elements) {
      obj[element.id] = element.value;
    }
    console.log(obj);
    fetch("/log/api/create", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(obj),
    })
      .then(async (res) => {
        if (res.status === 200) {
          location.reload();
        } else {
          const jsonresp = await res.json();
          showModal(jsonresp.message);
        }
      })
      .catch((e) => {
        showModal(e);
      });
  });
