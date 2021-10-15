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
          throw new Error("Response not ok");
        })
        .then((res) => {
          response.className = "form-text text-dark";
          response.textContent = "Hvala za prijavo!";
          console.log(res);
        })
        .catch((error) => {
          console.log(error);
          response.className = "form-text text-danger";
          response.textContent = "Napaka pri prijavi :(";
        })
        .then(() => {
          submitButton.removeAttribute("disabled");
          emailElem.removeAttribute("disabled");
          checkbox.removeAttribute("disabled");
        });
    });
  });
})();

(function () {
  var shareLinks = document.querySelectorAll(".share .share-box");
  shareLinks.forEach((shareLink) => {
    shareLink.addEventListener("click", function (event) {
      event.preventDefault();
      if (event.currentTarget.className.indexOf('isfbbox') != -1) {
        const url = `https://www.facebook.com/dialog/feed?app_id=831312620809085&redirect_uri=https%3A%2F%2Fhudapobuda.si&link=https%3A%2F%2Fhudapobuda.si&ref=responsive`;
        window.open(url, '_blank');
      }
      if (event.currentTarget.className.indexOf('isfbnoapp') != -1) {
        const url = `https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fhudapobuda.si`;
        window.open(url, 'pop', 'width=600, height=400, scrollbars=no');
      }
      if (event.currentTarget.className.indexOf('istwbox') != -1) {
        const url = `https://twitter.com/intent/tweet?text=${encodeURIComponent(window.SHARE_TWEET_TEXT + ' https://hudapobuda.si')}`;
        window.open(url, '_blank');
      }
      if (event.currentTarget.className.indexOf('istwinitiative') != -1) {
        const url = `https://twitter.com/intent/tweet?text=${encodeURIComponent(window.SHARE_TWEET_TEXT + ' ' + window.location.href)}`;
        window.open(url, '_blank');
      }
      if (event.currentTarget.className.indexOf('isembox') != -1) {
        const url = `mailto:?subject=${encodeURIComponent(window.SHARE_EMAIL_SUBJECT)}&body=${encodeURIComponent(window.SHARE_EMAIL_TEXT)}`;
        window.open(url, '_blank');
      }
    });
  });
})();

(function () {
  var forms = document.querySelectorAll('.needs-validation')
  forms.forEach(function (form) {
    form.style.scrollMarginTop = '120px';
    form.addEventListener('submit', function (event) {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
        form.scrollIntoView();
      }
      form.classList.add('was-validated');
    }, false);
  });
})();

(function () {
  const initiative_cards = document.querySelectorAll('.initiatives-section .box')
  initiative_cards.forEach(function (card) {
    const donation_id = card.getAttribute('data-donation-id')
    fetch(`https://podpri.djnd.si/api/donation-statistics/${donation_id}/`)
      .then(response => response.json())
      .then(data => {
        card.querySelector('.amount').textContent = data['donation-amount']
        const progressBarWidth = Math.round(parseInt(data['donation-amount']) / 5000 * 100)
        if (progressBarWidth > 0) {
          card.querySelector('.progress-bar').style.width = progressBarWidth + '%'
          card.querySelector('.progress-bar').style.display = 'block'
        }
      });
  })
})();

let donation_id;
let modalIFrame;
let modalMobileDonations;

(function () {
  const initiative_info = document.querySelector('.headline-initiative .initiative-info');
  if (initiative_info) {
    const podporniki = {
      0: 'podpornikov',
      1: 'podpornik',
      2: 'podpornika',
      3: 'podporniki',
      4: 'podporniki',
    }

    // dnevi
    const days = parseInt(initiative_info.querySelector('.days').textContent)
    if (days === 1) {
      initiative_info.querySelector('.days-text').textContent = 'dan'
    }
    donation_id = initiative_info.getAttribute('data-donation-id');
    fetch(`https://podpri.djnd.si/api/donation-statistics/${donation_id}/`)
      .then(response => response.json())
      .then(data => {
        const amount = parseInt(data['donation-amount'])
        const count = parseInt(data['donation-count'])
        initiative_info.querySelector('.amount').textContent = `${amount}`
        const progressBarWidth = Math.round(amount / 5000 * 100)
        if (progressBarWidth > 0) {
          initiative_info.querySelector('.progress-bar').style.width = progressBarWidth + '%'
          initiative_info.querySelector('.progress-bar').style.display = 'block'
        }
        initiative_info.querySelector('.count').textContent = `${count}`
        if (count < 5) {
          initiative_info.querySelector('.count-text').textContent = podporniki[count]
        }
      });
  }
})();

// donations
(function () {
  // modal
  const modalIFrameElement = document.getElementById('modal-iframe')
  if (modalIFrameElement) {
    modalIFrame = new bootstrap.Modal(modalIFrameElement, { show: false });
  }
  const modalMobileDonationsElement = document.getElementById('modal-mobile-donations')
  if (modalMobileDonationsElement) {
    modalMobileDonations = new bootstrap.Modal(modalMobileDonationsElement, { show: false });
  }

  const support_buttons = document.querySelectorAll('.support-button');
  support_buttons.forEach(function (sb) {
    sb.addEventListener('click',(event) => {
      support_buttons.forEach((button) => {
        button.classList.remove('selected');
        const input_f = button.querySelector('input')
        if (input_f) {
          input_f.classList.remove('error');
        }
      })
      let target = event.target;
      if (!target.classList.contains('support-button')) {
        target = target.parentNode;
      }
      target.classList.add('selected');
      if (!target.querySelector('input')) {
        setDonationLink();
      }
    })
  })
})();

function setDonationLink() {
  const selected_support_button = document.querySelector('.support-button.selected');
  let donation_amount;
  if (selected_support_button.querySelector('input')) {
    donation_amount = selected_support_button.querySelector('input').value;
    if (!donation_amount) {
      selected_support_button.querySelector('input').classList.add('error');
    }
  } else {
    donation_amount = selected_support_button.getAttribute('data-amount');
  }
  if (donation_amount && donation_id) {
    document.getElementById('donation-frame').setAttribute('src', `https://nov.djnd.si/doniraj_hudapobuda/placaj?amount=${donation_amount}&campaign=${donation_id}`);
    modalMobileDonations.hide();
    modalIFrame.show();
  }
}

function openDonations() {
  modalMobileDonations.show();
}

function selectLink(e) {
  const el = e.target;
  const sel = window.getSelection();
  if (sel.toString() === ''){ // no text selection
    window.setTimeout(function(){
      const range = document.createRange(); // range object
      range.selectNodeContents(el); // sets Range
      sel.removeAllRanges(); // remove all ranges from selection
      sel.addRange(range);// add Range to a Selection.
    },1);
  }
}
