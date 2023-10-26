window.addEventListener("load", function () {
  new Api().callApiLotDetail().then(new UI().showLotDetail);
});

class Api {
  async callApiLotDetail() {
    const urls=location.href.split('/')
    const lotId=urls[urls.length-1]
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
    getEl("name").setAttribute("value", lot[1]);
    getEl("name").setAttribute("value", lot[1]);
    getEl("address").innerHTML = lot[2];
    getEl("totalSpots").innerHTML = lot[3];
    getEl("availableSpots").innerHTML = lot[4];
    getEl("employee").innerHTML = lot[5];
  }
}
