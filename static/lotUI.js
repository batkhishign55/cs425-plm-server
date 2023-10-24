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

  showLots(apiresp) {
    let lotRows = [];
    for (let lot of apiresp.data) {
      let row = this.createRow(lot);
      lotRows.push(row);
    }

    this.loadPage(lotRows.join(""));
  }

  createRow(lot) {
    const cardTemplate = `
        <tr>
            <th scope="row">${lot[0]}</th>
            <td>${lot[1]}</td>
            <td>${lot[2]}</td>
            <td>${lot[4]}/${lot[3]}</td>
            <td>${lot[5]}</td>
            <td>
              <button type="button" class="btn btn-primary">Detail</button>
            </td>
        </tr>
        `;
    return cardTemplate;
  }
}
