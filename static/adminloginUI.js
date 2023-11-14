window.addEventListener("load", async function () {
  await fetch("/auth/admin/check", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  }).then((res) => {
    console.log(res);
    if (res.status == 200) {
      var base_url = window.location.origin;
      window.location.replace(base_url + "/lot");
    }
  });
});

document
  .getElementById("form")
  .addEventListener("submit", async function (evt) {
    evt.preventDefault();

    const elements = document.getElementById("form").elements;

    const obj = {};
    for (const element of elements) {
      obj[element.id] = element.value;
    }
    console.log(obj);

    fetch("/auth/admin/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(obj),
    })
      .then(async (res) => {
        if (res.status === 200) {
          var base_url = window.location.origin;
          window.location.replace(base_url + "/lot");
        } else {
          const jsonresp = await res.json();
          showModal(jsonresp.message);
        }
      })
      .catch((e) => {
        showModal(e);
      });
  });
