window.addEventListener("load", function () {
  // to-do check the session
  console.log("loaded");
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

    fetch("/auth/user/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(obj),
    })
      .then(async (res) => {
        if (res.status === 200) {
          var base_url = window.location.origin;
          window.location.replace(base_url + "/home");
        } else {
          const jsonresp = await res.json();
          document.getElementById("alert").innerHTML = jsonresp.message;
          document.getElementById("alert").style.display = "block";
        }
      })
      .catch((e) => {
        document.getElementById("alert").innerHTML = e;
        document.getElementById("alert").style.display = "block";
      });
  });
