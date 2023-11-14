var mode = "create";

window.addEventListener("load", async function () {
  const urls = location.href.split("/");
  const vehicleId = urls[urls.length - 1];

  // update mode
  if (vehicleId !== "") {
    mode = "update";

    const resp = await fetch(`/vehicle/api/detail/${vehicleId}`);
    const jsonresp = await resp.json();
    new UI().showvehicleDetail(jsonresp);
  }
});

document.getElementById("form").addEventListener(
  "submit",
  async function (evt) {
    evt.preventDefault();

    if (mode === "update") {
      const elements = document.getElementById("form").elements;

      const urls = location.href.split("/");
      const vehicleId = urls[urls.length - 1];
      const obj = { vehicleId };
      for (const element of elements) {
        obj[element.id] = element.value;
      }
      const resp = await fetch("/vehicle/api/update", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(obj),
      });

      const jsonresp = await resp.json();
    } // create
    else {
      const elements = document.getElementById("form").elements;

      const obj = {};
      for (const element of elements) {
        obj[element.id] = element.value;
      }
      const resp = await fetch("/vehicle/api/create", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(obj),
      });

      const jsonresp = await resp.json();
    }
    var base_url = window.location.origin;
    window.location.replace(base_url+"/");
  },
  true
);

class UI {
  constructor() {
    this.showvehicleDetail = this.showvehicleDetail.bind(this);
  }

  showvehicleDetail(apiresp) {
    const getEl = (id) => document.getElementById(id);
    const vehicle = apiresp.data;
    // getEl("vehicle ID").setAttribute("value", vehicle[0]);
    getEl("custID").setAttribute("value", vehicle[1]);
    getEl("plateNumber").setAttribute("value", vehicle[2]);
    getEl("type").setAttribute("value", vehicle[3]);
  }
}
