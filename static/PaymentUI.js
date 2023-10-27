window.addEventListener("load", function () {
    new Api().callApiLots().then(new UI().showPayments);
  });
  
  class Api {
    async callApiLots() {
      const resp = await fetch("/pay/api/");
      const jsonresp=await resp.json()
      return jsonresp;
    }
  }
  
  class UI {
    constructor() {
      this.showPayments = this.showPayments.bind(this);
    }
  
    loadPage(page) {
      let productListElement = document.getElementById("paymentListId");
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
              <td>${payment[3]}</td>
              <td>${payment[4]}</td>
              <td>${payment[5]}</td>
              
          </tr>
          `;
      return cardTemplate;
    }
  }
  