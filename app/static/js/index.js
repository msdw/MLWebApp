console.log("wa ww")

var stripe = Stripe('pk_test_6DkaDw0woAqDklauqEUb5rrH00503hwbWm');

var checkoutButton = document.querySelector('#checkout-button');
console.log(checkoutButton)
console.log("wa ww")
checkoutButton.addEventListener('click', function () {
  console.log("fuuuu")
  stripe.redirectToCheckout({
    items: [{
      // Define the product and SKU in the Dashboard first, and use the SKU
      // ID in your client-side code.
      sku: 'sku_FtR0v0Gp9zjJEp',
      quantity: 1
    }],
    successUrl: 'http://localhost:5000/index',
    cancelUrl: 'http://localhost:5000/index'
  });
});