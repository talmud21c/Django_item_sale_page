//* Form Validation
// Fetch all the forms we want to apply custom Bootstrap validation styles to
const forms = document.querySelectorAll('.needs-validation');

// Loop over them and prevent submission
Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        } else {
            const title = form.querySelector("#title").value;
            const author = form.querySelector("#author").value;
            const workId = form.querySelector("#workId").value;
            const amount = form.querySelector("#amount").value;
            const count = form.querySelector("#counter").value;
            const paymentId = form.querySelector("#paymentId").value;
            const walletAddress = form.querySelector("#walletAddress").value;

            if (confirm(`제목: ${title} \n작가: ${author} \n작품번호: ${workId} \n가격: ${amount} \n수량: ${count} \n결제번호: ${paymentId} \n지갑주소: ${walletAddress}`)) {
                return;
            } else {
                event.preventDefault();
                event.stopPropagation();
            }
        }

        form.classList.add('was-validated');
    }, false)
});


const countContainer = document.querySelector(".count-container");
const minusBtn = countContainer.querySelector("#minus-btn");
const plusBtn = countContainer.querySelector("#plus-btn");
const counter = countContainer.querySelector(".counter");
const amount = document.querySelector("#amount");
const defaultAmount = document.querySelector("#amount").value;
const availableQuantity = document.querySelector("#availableQuantity").innerText;

function init() {
    if (availableQuantity == 1) {
        minusBtn.setAttribute('disabled', 'disabled');
        plusBtn.setAttribute('disabled', 'disabled');
    }
}

init();

minusBtn.addEventListener("click", function () {
    // console.log(counter.value);
    /*    counter.value--;
        if (counter.value === '1') {
            setDisabled(this);
            amount.value = (defaultAmount * counter.value);
        } else if (counter.value === '2') {
            setAble(this);
            setAble(plusBtn);
            amount.value = (defaultAmount * counter.value);
        } else {
            setAble(this);
            amount.value = (defaultAmount * counter.value);
        }*/

    counter.value--;
    amount.value = (defaultAmount * counter.value);

    if (counter.value == 1) {
        setDisabled(this);
        setAble(plusBtn);
    }
});

plusBtn.addEventListener("click", function () {
    // console.log(counter.value);
    /*    counter.value++;
        if (counter.value === '1') {
            amount.value = (defaultAmount * counter.value);
        } else if (counter.value === '2') {
            setAble(minusBtn);
            amount.value = (defaultAmount * counter.value);
        } else {
            setDisabled(this);
            amount.value = (defaultAmount * counter.value);
        }*/

    counter.value++;
    amount.value = (defaultAmount * counter.value);

    if (availableQuantity == counter.value) {
        setDisabled(this);
        setAble(minusBtn);
    } else {
        setAble(this);
        setAble(minusBtn);
    }

});

function setDisabled(item) {
    item.setAttribute('disabled', 'disabled');
}

function setAble(item) {
    item.removeAttribute('disabled');
}
