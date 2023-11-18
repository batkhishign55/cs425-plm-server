window.addEventListener("load", function () {
    new Api().callApilogs().then(new UI().showlogs);
});
//CLASS
class Api {
async callApilogs() {
    const resp = await fetch("/log/api/");
    const jsonresp=await resp.json()
    console.log(jsonresp)
    return jsonresp;
}
}

class UI {
constructor() {
    this.showlogs = this.showlogs.bind(this);
}

loadPage(page) {
    let productListElement = document.getElementById("logListId");
    productListElement.innerHTML = page;
}

showlogs(apiresp) {
    let logRows = [];
    for (let log of apiresp.data) {
    let row = this.createRow(log);
    logRows.push(row);
    }

    this.loadPage(logRows.join(""));
}

createRow(log) {
    const cardTemplate = `
        <tr>
            <th scope="row">${log[0]}</th>
            <td>${log[1]}</td>
            <td>${log[2]}</td>
            <td>${log[3]}</td>
            <td>${log[4]}</td>
            <td>${log[5]}</td>
            
        </tr>
        `;
    return cardTemplate;
}
}