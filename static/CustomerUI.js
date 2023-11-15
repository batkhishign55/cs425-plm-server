window.addEventListener("load", function () {
    new Api().callApiCust().then(new UI().showCust);
  });
  
class Api {
  async callApiCust() {
    const resp = await fetch("/cust/api/");
    const jsonresp = await resp.json();
    return jsonresp;
  }

  async callDeleteCust(itemId) {

    const resp=await fetch('/cust/api/',
        {
            method:'DELETE',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({'custId':itemId})
        }
    )

    const jsonresp=await resp.json()
    this.callApiCust().then(new UI().showCust);
    return jsonresp;
  }
}
  
class UI {
  constructor() {
    this.showCust = this.showCust.bind(this);
  }
  
  loadPage(page) {
    let productListElement = document.getElementById("customerListId");
    productListElement.innerHTML = page;
  }
  
  showCust(apiresp) {
    let custRows = [];
    for (let cust of apiresp.data) {
      let row = this.createRow(cust);
      custRows.push(row);
    }

    this.loadPage(custRows.join(""));
    this.registerEventForDelete();
  }
  
  createRow(cust) {
    const custTemplate = `
        <tr>
            <th scope="row">${cust[0]}</th>
            <td>${cust[1]}</td>
            <td>${cust[2]}</td>
            <td>${cust[3]}</td>
            <td>${cust[4]}</td>
            <td>${cust[5]}</td>
            <td>${cust[6]}</td>
            <td>
            <a href="/cust/${cust[0]}">
              <button type="button" class="btn btn-primary">Update</button></a>
              <button type="button" class="btn btn-danger delete" itemId=${cust[0]}>Delete</button>
            
            </td>
        </tr>
        `;
    return custTemplate;
  }

  registerEventForDelete() {
    const listOfActionButton = document.getElementsByClassName("delete");

    for (let element of listOfActionButton) {
      element.addEventListener("click", function () {
        console.log(this.getAttribute("itemId"));
        new Api().callDeleteCust(this.getAttribute("itemId"));
      });
    }
  }
}

