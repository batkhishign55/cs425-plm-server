window.addEventListener("load", function () {
    new Api().callApiLots().then(new UI().showReservation);
  });
  
  class Api {
    async callApiLots() {
      const resp = await fetch("/res/api/");
      const jsonresp=await resp.json()
      return jsonresp;
    }
  }
  
  class UI {
    constructor() {
      this.showReservation = this.showReservation.bind(this);
    }
  
    loadPage(page) {
      let productListElement = document.getElementById("reservationListId");
      productListElement.innerHTML = page;
    }
  
    showReservation(apiresp) {
      let ReservationRows = [];
      for (let reservation of apiresp.data) {
        let row = this.createRow(reservation);
        ReservationRows.push(row);
      }
  
      this.loadPage(ReservationRows.join(""));
    }
  
    createRow(reservation) {
      const cardTemplate = `
          <tr>
              <th scope="row">${reservation[0]}</th>
              <td>${reservation[2]}</td>
              <td>${reservation[3]}</td>
              <td>${reservation[4]}</td>
              <td>${reservation[5]}</td>
          </tr>
          `;
      return cardTemplate;
    }
  }
  