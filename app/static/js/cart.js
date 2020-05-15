if (document.readyState == 'loading'){
  document.addEventListener('DOMContentLoaded', ready)
} else{
  ready()
}

function ready(){
  let removeCartItemButtons = document.getElementsByClassName('btn-danger')
  for (var i = 0; i < removeCartItemButtons.length; i++) {
    let button = removeCartItemButtons[i]
    button.addEventListener('click', removeCartItem)
  }

  let quantityInputs = document.getElementsByClassName('cart-quantity-input')
  for(var i = 0; i < quantityInputs.length; i++){
    let input = quantityInputs[i]
    input.addEventListener('change', quantityChanged)
  }

  let addToCartButton = document.getElementsByClassName('shop-item-button')
  for(var i = 0; i < addToCartButton.length; i++){
    let button = addToCartButton[i]
    button.addEventListener('click', addToCartClicked)
  }

  document.getElementsByClassName('btn-purchase')[0].addEventListener('click', purchaseClicked)

}

function purchaseClicked(){
  alert('Thank you for your purchase')
    var cartItems = document.getElementsByClassName('cart-items')[0]
    while (cartItems.hasChildNodes()) {
        cartItems.removeChild(cartItems.firstChild)
    }
    updateCartTotal()
}

function removeCartItem(event){
  let buttonClicked = event.target
    buttonClicked.parentElement.parentElement.remove()
    updateCartTotal()
}

function quantityChanged(event){
  let input = event.target
  if (isNaN(input.value) || input.value <= 0){
    input.value = 1
  }
  updateCartTotal()
}

function addToCartClicked(event){
  let button = event.target
  let menuItem = button.parentElement.parentElement.parentElement
  let title = menuItem.getElementsByClassName('shop-item-title')[0].innerText
  let price = menuItem.getElementsByClassName('shop-item-price')[0].innerText
  console.log(title, price)
  addItemToCart(title, price)
  updateCartTotal()
}

function addItemToCart(title, price){
  let cartRow = document.createElement('div')
  let cartItems = document.getElementsByClassName('cart-items')[0]
  let cartItemNames = cartItems.getElementsByClassName('cart-item-title')
  for (var i = 0; i < cartItemNames.length; i++){
    if (cartItemNames[i].innerText == title){
      alert("This item has already been added to the cart")
      return
    }
  }
  let  cartRowContents = `
      <div class="cart-row">
        <div class="cart-item-title cart-column">
          ${title}
        </div>
        <span class="cart-price cart-column">${ price }</span>
        <div class="cart-quantity cart-column">
          <input class="cart-quantity-input" type="number" value="1" min="1">
          <button class="btn btn-danger" type="button">REMOVE</button>
        </div>
    </div>
  `
  cartRow.innerHTML = cartRowContents
  cartItems.append(cartRow)
  cartRow.getElementsByClassName('btn-danger')[0].addEventListener('click', removeCartItem)
  cartRow.getElementsByClassName('cart-quantity-input')[0].addEventListener('change', quantityChanged)
}


function updateCartTotal() {
  let cartItemContainer = document.getElementsByClassName('cart-items')[0]
  let cartRows = cartItemContainer.getElementsByClassName('cart-row')
  let total = 0
  for (let i = 0; i < cartRows.length; i++) {
    let cartRow = cartRows[i]
    let priceElement = cartRow.getElementsByClassName('cart-price')[0]
    let quantityElement = cartRow.getElementsByClassName('cart-quantity-input')[0]
    // let price = parseInt(priceElement.innerText.replace('ksh', ''))
    // let quantity = parseInt(quantityElement.value)
    let price = parseInt(priceElement.innerText)
    let quantity = parseInt(quantityElement.value)
    console.log(typeof(price))
    console.log(typeof(quantity))
    console.log(typeof(total))

    // total = total + quantity
    total = total + price
    
    console.log(typeof(total))
  }
  document.getElementsByClassName("cart-total-price")[0].innerText = 'kshs ' +  total 
}

function createOrder() {
  const cartItems = [];

  let cartItemContainer = document.getElementsByClassName('cart-items')[0]
  let cartRows = cartItemContainer.getElementsByClassName('cart-row')

  for (let i = 0; i < cartRows.length; i++) {
    let cartRow = cartRows[i]
    cartItems.push({
      id: cartRow.id
    })
  }

  fetch("/menu", {
    method: "post",
    body: JSON.stringify(cartItems),
    headers: {
      'Content-Type': 'application/json'
    },
  }).then(function (res) {
    alert("Order created successfully");
  }).catch(function (err) {
    alert(err);
  });
}