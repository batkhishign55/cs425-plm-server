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
      await fetch("/vehicle/api/update", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(obj),
      })
        .then(async (res) => {
          if (res.status === 200) {
            var base_url = window.location.origin;
            window.location.replace(base_url + "/vehicle");
          } else {
            const jsonresp = await res.json();
            showModal(res.status + " " + jsonresp.message);
          }
        })
        .catch((e) => {
          showModal(e);
        });
    } // create
    else {
      const elements = document.getElementById("form").elements;

      const obj = {};
      for (const element of elements) {
        obj[element.id] = element.value;
      }

      await fetch("/vehicle/api/create", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(obj),
      })
        .then(async (res) => {
          if (res.status === 200) {
            var base_url = window.location.origin;
            window.location.replace(base_url + "/vehicle");
          } else {
            const jsonresp = await res.json();
            showModal(res.status + " " + jsonresp.message);
          }
        })
        .catch((e) => {
          showModal(e);
        });
    }
  },
  true
);

class UI {
  constructor() {
    this.showvehicleDetail = this.showvehicleDetail.bind(this);
  }

  showvehicleDetail(apiresp) {
    const vehicle = apiresp.data;
    document.getElementById("plateNumber").setAttribute("value", vehicle[2]);
    var typeEl = document.getElementById("type");
    typeEl.value = vehicle[3];
  }
}
