window.addEventListener("load", function () {
});

document.getElementById("logout").addEventListener("click", async function () {
  const resp = await fetch("/auth/logout", {
    method: "POST",
  });

  const jsonresp = await resp.json();
  var base_url = window.location.origin;
  window.location.replace(base_url + "/");
});
