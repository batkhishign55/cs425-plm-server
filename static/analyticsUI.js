window.addEventListener("load", function () {
  new Api().callApiLots().then(new UI().showList);
});

class Api {
  async callApiLots() {
    return await fetch("/pay/api/analytics/")
      .then(async (res) => {
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
}

class UI {
  constructor() {
    this.showList = this.showList.bind(this);
  }

  loadPage(page) {
    let productListElement = document.getElementById("lotListId");
    productListElement.innerHTML = page;
  }

  showList(apiresp) {
    let payRows = [];
    for (let pay of apiresp.data) {
      let row = this.createRow(pay);
      payRows.push(row);
    }

    this.loadPage(payRows.join(""));
    this.calcAnalysis(apiresp);
  }

  calcAnalysis(apiresp) {
    let custs = [];
    let methods = [[], [], [], [], []];
    let methods_sum = [0, 0, 0, 0, 0];
    for (let pay of apiresp.data) {
      if (pay[0] == null) {
        continue;
      }
      if (!custs.includes(pay[0])) {
        custs.push(pay[0]);

        methods.forEach(function (arr, i) {
          methods[i].push(pay[1]);
        });
      }
      switch (pay[1]) {
        case "credit":
          methods[0][methods[0].length - 1] = parseInt(pay[2]);
          methods_sum[0] += parseInt(pay[2]);
          break;
        case "debit":
          methods[1][methods[1].length - 1] = parseInt(pay[2]);
          methods_sum[1] += parseInt(pay[2]);
          break;
        case "google pay":
          methods[2][methods[2].length - 1] = parseInt(pay[2]);
          methods_sum[2] += parseInt(pay[2]);
          break;
        case "apple pay":
          methods[3][methods[3].length - 1] = parseInt(pay[2]);
          methods_sum[3] += parseInt(pay[2]);
          break;
        case "cash":
          methods[4][methods[4].length - 1] = parseInt(pay[2]);
          methods_sum[4] += parseInt(pay[2]);
          break;
        default:
          break;
      }
    }
    const ctx = document.getElementById("barChart");

    new Chart(ctx, {
      type: "bar",
      data: {
        labels: custs,
        datasets: [
          {
            label: "Credit",
            data: methods[0],
            backgroundColor: "rgb(255, 99, 132)",
          },
          {
            label: "Debit",
            data: methods[1],
            backgroundColor: "rgb(54, 162, 235)",
          },
          {
            label: "Google Pay",
            data: methods[2],
            backgroundColor: "rgb(75, 192, 192)",
          },
          {
            label: "Apple Pay",
            data: methods[3],
            backgroundColor: "rgb(75, 150, 89)",
          },
          {
            label: "Cash",
            data: methods[4],
            backgroundColor: "rgb(255, 205, 86)",
          },
        ],
      },
      options: {
        plugins: {
          title: {
            display: true,
            text: "Payment methods by each user",
          },
        },
        responsive: true,
        scales: {
          x: {
            stacked: true,
          },
          y: {
            stacked: true,
          },
        },
      },
    });

    const ctx2 = document.getElementById("donutChart");

    new Chart(ctx2, {
      type: "doughnut",
      data: {
        labels: ["Credit", "Debit", "Google Pay", "Apple Pay", "Cash"],
        datasets: [
          {
            label: "Dataset",
            data: methods_sum,
            backgroundColor: [
              "rgb(255, 99, 132)",
              "rgb(54, 162, 235)",
              "rgb(75, 192, 192)",
              "rgb(75, 150, 89)",
              "rgb(255, 205, 86)",
            ],
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: "top",
          },
          title: {
            display: true,
            text: "Payment methods distribution",
          },
        },
      },
    });
  }

  createRow(payment) {
    payment[0] = payment[0] == null ? "" : payment[0];
    payment[1] = payment[1] == null ? "" : payment[1];
    payment[2] = payment[2] == null ? "" : payment[2];
    const cardTemplate = `
          <tr>
              <th scope="row">${payment[0]}</th>
              <td>${payment[1]}</td>
              <td>$${payment[2]}</td>
              
          </tr>
          `;
    return cardTemplate;
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
