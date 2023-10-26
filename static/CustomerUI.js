window.addEventListener("load", function () {
    new Api().callApiLots().then(new UI().showCust);
  });
  
  class Api {
    async callApiLots() {
      const resp = await fetch("/cust/api/");
      const jsonresp=await resp.json()
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
              <td>${cust[7]}</td>
              <td>
              <a href="/cust/${cust[0]}">
                <button type="button" class="btn btn-primary">Update</button>
              </a>
              </td>
          </tr>
          `;
      return custTemplate;
    }
  }
  