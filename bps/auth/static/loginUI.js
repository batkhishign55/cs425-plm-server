window.addEventListener("load", function () {});

document
  .getElementById("form")
  .addEventListener("submit", async function (evt) {
    evt.preventDefault();

    const elements = document.getElementById("form").elements;

    const obj = {};
    for (const element of elements) {
      obj[element.id] = element.value;
    }
    const resp = fetch("/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(obj),
    })
      .then((res) => {
        if (res.status === 200) {
          var base_url = window.location.origin;
          window.location.replace(base_url + "/");
        }
      })
      .catch((e) => {
        console.log("some error occured");
      });
  });
