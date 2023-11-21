window.addEventListener("load", function () {
    new Api().callApiVehicle().then(new UI().showVehicle);
  });
  
  class Api {
    async callApiVehicle() {
      const resp = await fetch("/vehicle/api/");
      const jsonresp = await resp.json();
      return jsonresp;
    }
  
    async callDeleteVehicle(itemId) {
  
      const resp=await fetch('/vehicle/api/',
          {
              method:'DELETE',
              headers:{
                  'Content-Type':'application/json'
              },
              body:JSON.stringify({'vehicleId':itemId})
          }
      )
  
      const jsonresp=await resp.json()
      this.callApiVehicle().then(new UI().showVehicle);
      return jsonresp;
    }
  }
  
  class UI {
    constructor() {
      this.showVehicle = this.showVehicle.bind(this);
    }
  
    loadPage(page) {
      let productListElement = document.getElementById("vehicleListId");
      productListElement.innerHTML = page;
    }
  
    showVehicle(apiresp) {
      let vehicleRows = [];
      for (let vehicle of apiresp.data) {
        let row = this.createRow(vehicle);
        vehicleRows.push(row);
      }
  
      this.loadPage(vehicleRows.join(""));
      this.registerEventForDelete();
    }
  
    createRow(vehicle) {
      const cardTemplate = `
          <tr>
              <th scope="row">${vehicle[0]}</th>
              <td>${vehicle[2]}</td>
              <td>${vehicle[3]}</td>
              <td>
                <a href="/vehicle/${vehicle[0]}">
                  <button type="button" class="btn btn-primary">Update</button>
                </a>
                <button type="button" class="btn btn-danger delete" itemId=${vehicle[0]}>Delete</button>
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
          new Api().callDeleteVehicle(this.getAttribute("itemId"));
        });
      }
    }
  }
  
