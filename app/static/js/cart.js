let removeCartItem = document.getElementsByClassName('btn-danger')
console.log(removeCartItem)
for (var i=0; i < removeCartItem.length; i++){
  let button = removeCartItem[i]
  button.addEventListener('click', function(event){
    let buttonClicked = event.target
    buttonClicked.parentElement.parentElement.remove()
  })
}

function updateCartTotal(){
  let cartItemContainer = document.getElementsByClassName('cart-items')[0]
  let cartRows = cartItemContainer.getElementsByClassName('cart-row')
  for(let i = 0; i < cartRows.length; i++){
    let cartRow = cartRows[i]
    let riceElement = cartRow.getElementsByClassName('cart-price')[0]
    
  }
}