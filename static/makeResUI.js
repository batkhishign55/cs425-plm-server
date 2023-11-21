window.addEventListener("load", function () {
  new Api().callApiLots().then(new UI().showLots);
  document
    .getElementById("startTime")
    .addEventListener("input", updateTotalDuration);
  document
    .getElementById("endTime")
    .addEventListener("input", updateTotalDuration);
});

let jsonrespsave = [];
let selected;

class Api {
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

class UI {
  constructor() {
    this.showLots = this.showLots.bind(this);
  }

  loadPage(page) {
    let dropdown = document.getElementById("lotListId");
    dropdown.innerHTML = page;
  }

  showLots(apiresp) {
    let lotRows = [];
    for (let lot of apiresp.data) {
      let row = this.createRow(lot);
      lotRows.push(row);
    }

    this.loadPage(lotRows.join(""));
  }

  createRow(lot) {
    const cardTemplate = `
      <li><a class="dropdown-item" href="#" onclick="itemPressedd(${lot[0]})">${lot[0]}, ${lot[1]}, ${lot[2]}, ${lot[5]}</a></li>`;
    return cardTemplate;
  }
}

$(document).ready(function () {
  $("#searchInput").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    let dropdown = document.getElementById("lotListId");
    if (value == "" || value == null) {
      $(dropdown).removeClass("show");
    } else {
      $(dropdown).addClass("show");
    }

    $("#lotListId li").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
});

function updateTotalDuration() {
  const startTime = new Date(document.getElementById("startTime").value);
  const endTime = new Date(document.getElementById("endTime").value);

  if (!isNaN(startTime) && !isNaN(endTime) && endTime > startTime) {
    const durationInMinutes = (endTime - startTime) / (1000 * 60);
    const hours = Math.floor(durationInMinutes / 60);
    const minutes = Math.round(durationInMinutes % 60);

    if (hours >= 24) {
      const days = Math.floor(hours / 24);
      document.getElementById("totalDuration").value = `${days} day(s) ${
        hours % 24
      } hours ${minutes} minutes`;
    } else {
      document.getElementById(
        "totalDuration"
      ).value = `${hours} hours ${minutes} minutes`;
    }

  } else {
    document.getElementById("totalDuration").value = "";
  }
}

function itemPressedd(lotId) {
  selected = lotId;
  let dropdown = document.getElementById("lotListId");
  $(dropdown).removeClass("show");

  const res = jsonrespsave.filter((lot) => lot[0] === lotId)[0];
  console.log(res);
  document.getElementById(
    "searchInput"
  ).value = `${res[0]}, ${res[1]}, ${res[2]}, ${res[5]}`;
}

document
  .getElementById("form")
  .addEventListener("submit", async function (evt) {
    evt.preventDefault();
    const elements = document.getElementById("form").elements;

    const obj = {};
    for (const element of elements) {
      obj[element.id] = element.value;
    }
    obj['lotId'] = selected;
    console.log(obj);
    fetch("/res/api/create", {
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
