window.addEventListener("load", function () {
    new Api().callApiReservation().then(new UI().showReservation);
  });
  
  class Api {
    async callApiReservation() {
      const resp = await fetch("/reservation/api/");
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
  
      this.loadPage(lotRows.join(""));
    }
  
    createRow(lot) {
      const cardTemplate = `
          <tr>
              <th scope="row">${reservation[0]}</th>
              <td>${reservation[1]}</td>
              <td>${reservation[2]}</td>
              <td>${reservation[4]}/${reservation[3]}</td>
              <td>${reservation[5]}</td>
              <td>
                <button type="button" class="btn btn-primary">Detail</button>
              </td>
          </tr>
          `;
      return cardTemplate;
    }
  }
  