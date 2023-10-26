window.addEventListener("load", function () {
    new Api().callApiCustDetail().then(new UI().showCustDetail);
  });
  
  class Api {
    async callApiCustDetail() {
      const urls=location.href.split('/')
      const lotId=urls[urls.length-1]
      const resp = await fetch(`/cust/api/detail/${custId}`);
      const jsonresp = await resp.json();
      return jsonresp;
    }
  }
  
  class UI {
    constructor() {
      this.showCustDetail = this.showCustDetail.bind(this);
    }
  
    showCustDetail(apiresp) {
      const getEl = (id) => document.getElementById(id);
      const customer = apiresp.data;
      getEl("name").setAttribute("value", customer[1]);
      getEl("name").setAttribute("value", customer[1]);
      getEl("name").setAttribute("value", customer[1]);
      getEl("address").innerHTML = customer[2];
      getEl("totalSpots").innerHTML = customer[3];
      getEl("availableSpots").innerHTML = customer[4];
      getEl("employee").innerHTML = customer[5];
    }
  }
  