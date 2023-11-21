window.addEventListener("load", async function () {
  await fetch("/cust/api/allusers/")
    .then(async (res) => {
      if (res.status === 200) {
        const jsonresp = await res.json();
        showValues(jsonresp.data);
      } else {
        const jsonresp = await res.json();
        showModal(res.status + " " + jsonresp.message);
      }
    })
    .catch((e) => {
      showModal(e);
    });
});

function showValues(data) {
  let rows = [];
  for (const user of data) {
    const row = createRow(user);
    rows.push(row);
  }

  let productListElement = document.getElementById("userListId");
  productListElement.innerHTML = rows.join("");
}

function createRow(row) {
  const cardTemplate = `
          <tr id=${row[0]}>
              <th scope="row">${row[0]}</th>
              <td>${row[1]}</td>
              <td>${row[2]}</td>
              <td>${row[3]}</td>
              <td>${row[4]}</td>
              <td>${row[5]}</td>
          </tr>
          `;
  return cardTemplate;
}
