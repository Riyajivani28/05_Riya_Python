// PayEase Client-Side JavaScript Logic

document.addEventListener('DOMContentLoaded', function () {
    // 1. Dynamic Total Amount Calculation for Pay / Checkout Forms
    const quantityInput = document.getElementById('quantity');
    const unitPriceElement = document.getElementById('unitPrice');
    const totalAmountElement = document.getElementById('totalAmount');
    const totalAmountInput = document.getElementById('totalAmountInput');

    if (quantityInput && unitPriceElement && totalAmountElement) {
        const unitPrice = parseFloat(unitPriceElement.dataset.price || unitPriceElement.innerText.replace(/[^0-9.]/g, '')) || 0;

        function updateTotal() {
            let qty = parseInt(quantityInput.value) || 1;
            if (qty < 1) {
                qty = 1;
                quantityInput.value = 1;
            }
            const maxQty = parseInt(quantityInput.getAttribute('max'));
            if (maxQty && qty > maxQty) {
                qty = maxQty;
                quantityInput.value = maxQty;
                alert(`Maximum available quantity is ${maxQty}`);
            }

            const total = (unitPrice * qty).toFixed(2);
            totalAmountElement.innerText = `₹${total}`;
            if (totalAmountInput) {
                totalAmountInput.value = total;
            }
        }

        quantityInput.addEventListener('input', updateTotal);
        quantityInput.addEventListener('change', updateTotal);
        updateTotal(); // Run initial calculation on page load
    }

    // 2. Client-side Form Validation
    const checkoutForms = document.querySelectorAll('.needs-validation');
    checkoutForms.forEach(form => {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
});
