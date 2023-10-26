window.addEventListener("load", function () {
    new Api().callApiLots().then(new UI().showLots);
  });
  
  class Api {
    async callApiLots() {
      const resp = await fetch("/lot/api/");
      const jsonresp=await resp.json()
      return jsonresp;
    }
  }
  
  class UI {
    constructor() {
      this.showLots = this.showLots.bind(this);
    }
  
    loadPage(page) {
      let productListElement = document.getElementById("lotListId");
      productListElement.innerHTML = page;
    }
  
    showPayments(apiresp) {
      let paymentRows = [];
      for (let payment of apiresp.data) {
        let row = this.createRow(payment);
        paymentRows.push(row);
      }
  
      this.loadPage(paymentRows.join(""));
    }
  
    createRow(payment) {
      const cardTemplate = `
          <tr>
              <th scope="row">${payment[0]}</th>
              <td>${payment[1]}</td>
              <td>${payment[2]}</td>
              <td>${payment[4]}/${payment[3]}</td>
              <td>${payment[5]}</td>
              <td>
                <button type="button" class="btn btn-primary">Detail</button>
              </td>
          </tr>
          `;
      return cardTemplate;
    }
  }
  