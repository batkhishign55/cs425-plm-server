window.addEventListener("load", function () {
  new Api().callApiLotDetail().then(new UI().showLotDetail);
});

document.getElementById("form").addEventListener(
  "submit",
  async function (evt) {
    evt.preventDefault();
    const elements = document.getElementById("form").elements;

    const urls = location.href.split("/");
    const lotId = urls[urls.length - 1];
    const obj = { lotId };
    for (const element of elements) {
      obj[element.id] = element.value;
    }
    const resp = await fetch("/lot/api/update", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(obj),
    });

    const jsonresp = await resp.json();
  },
  true
);

class Api {
  async callApiLotDetail() {
    const urls = location.href.split("/");
    const lotId = urls[urls.length - 1];
    const resp = await fetch(`/lot/api/detail/${lotId}`);
    const jsonresp = await resp.json();
    return jsonresp;
  }
}

class UI {
  constructor() {
    this.showLotDetail = this.showLotDetail.bind(this);
  }

  showLotDetail(apiresp) {
    const getEl = (id) => document.getElementById(id);
    const lot = apiresp.data;
    getEl("name").setAttribute("value", lot[1]);
    getEl("location").setAttribute("value", lot[2]);
    getEl("totalSpots").setAttribute("value", lot[3]);
    getEl("availableSpots").setAttribute("value", lot[4]);
    getEl("employee").setAttribute("value", lot[5]);
  }

  showLotDetail(apiresp) {
    const getEl = (id) => document.getElementById(id);
    const lot = apiresp.data;
    getEl("name").setAttribute("value", lot[1]);
    getEl("location").setAttribute("value", lot[2]);
    getEl("totalSpots").setAttribute("value", lot[3]);
    getEl("availableSpots").setAttribute("value", lot[4]);
    getEl("employee").setAttribute("value", lot[5]);
  }
}
