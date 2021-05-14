(function () {
  var newsletterElems = document.querySelectorAll(".newsletter");
  newsletterElems.forEach(function (newsletterElem) {
    var form = newsletterElem.querySelector("form");
    var emailElem = form.querySelector("#email");
    var submitButton = form.querySelector("button[type='submit']");
    var checkbox = form.querySelector("#confirm-email");
    var response = form.querySelector("#response");
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      submitButton.setAttribute("disabled", "disabled");
      emailElem.setAttribute("disabled", "disabled");
      checkbox.setAttribute("disabled", "disabled");
      fetch("https://podpri.djnd.si/api/subscribe/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: emailElem.value,
          segment: 17,
        }),
      })
        .then((res) => {
          if (res.ok) {
            return res.text();
          }
          throw new Error('Response not ok');
        })
        .then((res) => {
          response.className = 'form-text text-dark';
          response.textContent = 'Hvala za prijavo!';
          console.log(res);
        })
        .catch((error) => {
          console.log(error);
          response.className = 'form-text text-danger';
          response.textContent = 'Napaka pri prijavi :(';
        })
        .then(() => {
          submitButton.removeAttribute("disabled");
          emailElem.removeAttribute("disabled");
          checkbox.removeAttribute("disabled");
        });
    });
  });
})();
