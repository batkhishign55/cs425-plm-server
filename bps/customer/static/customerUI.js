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
      const cust = apiresp.data;
      getEl("name").setAttribute("value", cust[1]);
      getEl("name").setAttribute("value", cust[1]);
      getEl("name").setAttribute("value", cust[1]);
      getEl("address").innerHTML = cust[2];
      getEl("totalSpots").innerHTML = cust[3];
      getEl("availableSpots").innerHTML = cust[4];
      getEl("employee").innerHTML = cust[5];
    }
  }
  