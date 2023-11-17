var mode = "create";

window.addEventListener("load", async function () {
  const urls = location.href.split("/");
  const custId = urls[urls.length - 1];

  // update mode
  if (custId !== "") {
    mode = "update";

    const resp = await fetch(`/cust/api/detail/${custId}`);
    const jsonresp = await resp.json();
    //console.log(jsonresp)
    new UI().showCustDetail(jsonresp);
  }
});

// window.addEventListener("load", function () {
//     new Api().callApiCustDetail().then(new UI().showCustDetail);
//   });

document.getElementById("form").addEventListener(
  "submit",
  async function (evt) {
    evt.preventDefault();

    if(mode=="update"){
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
  }//create
  else{
    const elements = document.getElementById("form").elements;

      const obj = {};
      for (const element of elements) {
        obj[element.id] = element.value;
      }
      const resp = await fetch("/cust/api/create", {
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
    this.showCustDetail = this.showCustDetail.bind(this);
  }

  showCustDetail(apiresp) {
    const getEl = (id) => document.getElementById(id);
    const customer = apiresp.data;
    console.log();
    getEl("first_name").setAttribute("value", customer[1]);
    getEl("last_name").setAttribute("value", customer[2]);
    getEl("email").setAttribute("value", customer[3]);
    getEl("phone_number").setAttribute("value", customer[4]);
    getEl("address").setAttribute("value", customer[5]);
    getEl("username").setAttribute("value", customer[6]);
    getEl("password").setAttribute("value", customer[7]);
  }


  
}
  