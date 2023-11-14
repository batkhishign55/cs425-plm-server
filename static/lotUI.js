window.addEventListener("load", function () {
  new Api().callApiLots().then(new UI().showLots);
});

class Api {
  async callApiLots() {
    return await fetch("/lot/api/").then(async (res) => {
      if (res.status === 200) {
        const jsonresp = await res.json();
        return jsonresp;
      } else {
        const jsonresp = await res.json();
        showModal(res.status + " " + jsonresp.message);
      }
    })
    .catch((e) => {
      showModal(e);
    });
  }

  async callDeleteLot(itemId) {
    const resp = await fetch("/lot/api/", {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ lotId: itemId }),
    });

    const jsonresp = await resp.json();
    this.callApiLots().then(new UI().showLots);
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
    this.registerEventForDelete();
  }

  createRow(lot) {
    const cardTemplate = `
        <tr>
            <th scope="row">${lot[0]}</th>
            <td>${lot[1]}</td>
            <td>${lot[2]}</td>
            <td>${lot[4]}/${lot[3]}</td>
            <td>${lot[6]} ${lot[7]}</td>
            <td>
              <a href="/lot/${lot[0]}">
                <button type="button" class="btn btn-primary">Update</button>
              </a>

              <button type="button" class="btn btn-danger delete" itemId=${lot[0]}>Delete</button>
            </td>
        </tr>
        `;
    return cardTemplate;
  }

  registerEventForDelete() {
    const listOfActionButton = document.getElementsByClassName("delete");

    for (let element of listOfActionButton) {
      element.addEventListener("click", function () {
        console.log(this.getAttribute("itemId"));
        new Api().callDeleteLot(this.getAttribute("itemId"));
      });
    }
  }
}

$(document).ready(function () {
  $("#searchInput").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#lotListId tr").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
});
