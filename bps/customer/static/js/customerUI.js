window.addEventListener("load", function () {
    new Api().callApiCustDetail().then(new UI().showCustDetail);
  });

document.getElementById("form").addEventListener(
  "submit",
  async function (evt) {
    evt.preventDefault();
    const elements = document.getElementById("form").elements;

    const urls = location.href.split("/");
    const custId = urls[urls.length - 1];
    const obj = { custId };
    for (const element of elements) {
      obj[element.id] = element.value;
    }
    const resp = await fetch("/cust/api/update", {
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
    getEl("fname").setAttribute("value", customer[1]);
    getEl("lname").setAttribute("value", customer[2]);
    getEl("email").setAttribute("value", customer[3]);
    getEl("phone_number").setAttribute("value", customer[4]);
    getEl("address").setAttribute("value", customer[5]);
    getEl("username").setAttribute("value", customer[6]);
    getEl("password").setAttribute("value", customer[7]);
  }

  
}
  