console.log("wa ww")

var stripe = Stripe('pk_test_6DkaDw0woAqDklauqEUb5rrH00503hwbWm');

var elements = stripe.elements();
var cardElement = elements.create('card');
cardElement.mount('#card-element');

// var checkoutButton = document.querySelector('#checkout-button');
// console.log(checkoutButton)
// console.log("wa ww")
// checkoutButton.addEventListener('click', function () {
//   console.log("fuuuu")
//   stripe.redirectToCheckout({
//     items: [{
//       // Define the product and SKU in the Dashboard first, and use the SKU
//       // ID in your client-side code.
//       sku: 'sku_FtR0v0Gp9zjJEp',
//       quantity: 1
//     }],
//     successUrl: 'http://localhost:5000/index',
//     cancelUrl: 'http://localhost:5000/index'
//   });
// });


var cardholderName = document.getElementById('cardholder-name');
var cardButton = document.getElementById('card-button');
var clientSecret = cardButton.dataset.secret;

cardButton.addEventListener('click', function(ev) {
  stripe.handleCardPayment(
    clientSecret, cardElement, {
      payment_method_data: {
        billing_details: {name: cardholderName.value}
      }
    }
  ).then(function(result) {
    if (result.error) {
      // Display error.message in your UI.
    } else {
      // The payment has succeeded. Display a success message.
    }
  });
});