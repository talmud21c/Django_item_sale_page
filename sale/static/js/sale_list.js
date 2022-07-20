const amount = document.querySelectorAll('.amount');

Array.from(amount).forEach((el) => {
    el.innerText = el.innerText.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",");
})
