window.addEventListener("load", function () {
  fetch("/log/api/parking")
    .then(async (res) => {
      if (res.status === 200) {
        const jsonresp = await res.json();
        showValues(jsonresp.data);
      } else if (res.status === 404) {
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
  for (const log of data) {
    const row = createRow(log);
    rows.push(row);
  }

  let productListElement = document.getElementById("logListId");
  productListElement.innerHTML = rows.join("");
}

function updateDuration(datetime) {
  var startTime = new Date(datetime);

  var timeDifference = new Date() - startTime;

  var days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
  var hours = Math.floor(
    (timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
  );
  var minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

  return days + "d " + hours + "h " + minutes + "m " + seconds + "s";
}

function createRow(log) {
  const cardTemplate = `
        <tr id=${log[0]}>
            <th scope="row">${log[0]}</th>
            <td>${log[1]}</td>
            <td>${log[2]}</td>
            <td>${log[3]}</td>
            <td>${log[5]}</td>
            <td>
                <button type="button" class="btn btn-primary" onclick="exit(${log[0]})">Exit</button>
            </td>
        </tr>
        `;
  return cardTemplate;
}

function exit(logId) {
  var div = document.getElementById("formContainer");

  if (div.style.display === "none") {
    div.style.display = "block";
  }

  document.getElementById("logId").setAttribute("value", logId);
  var row = document.getElementById(logId);

  var startTime = new Date(row.cells[3].innerHTML);

  var timeDifference = new Date() - startTime;

  var days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
  var hours = Math.floor(
    (timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
  );
  var minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);

  document
    .getElementById("duration")
    .setAttribute(
      "value",
      days + "d " + hours + "h " + minutes + "m " + seconds + "s"
    );
  document
    .getElementById("pmtAmt")
    .setAttribute("value", Math.ceil(timeDifference / (1000 * 60 * 60)) * 5);
}

document.getElementById("form3").addEventListener(
  "submit",
  async function (evt) {
    const elements = document.getElementById("form3").elements;

    const obj = {};
    for (const element of elements) {
      obj[element.id] = element.value;
    }
    await fetch("/pay/api/make", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(obj),
    })
      .then(async (res) => {
        if (res.status === 200) {
          location.reload();
        } else {
          const jsonresp = await res.json();
          showModal(res.status + " " + jsonresp.message);
        }
      })
      .catch((e) => {
        showModal(e);
      });
  },
  true
);
