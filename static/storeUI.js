
window.addEventListener('load',function(){
    new Api().callApiProducts().then(new UI().showProducts)
})


class Api{

    async callApiProducts(){
        const resp=await fetch('/product/api/')
        const jsonresp=await resp.json()
        return jsonresp
    }

    async addNewItem(itemId){
        const resp=await fetch('/cart/api/',
            {
                method:'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body:JSON.stringify({'productId':itemId})
            }
        )

        const jsonresp=await resp.json()
        new ApiNotif().callApiCartNotif().then(new UINotif().showCartNotif)
    }

}

class UI{
    constructor(){
        this.showProducts=this.showProducts.bind(this)
    }
    
    loadPage(page){
        let productListElement=document.getElementById('productListId')
        productListElement.innerHTML=page
    }

    showProducts(apiresp){
        let productCards=[]
        for (let product of apiresp.data){
            let card=this.createCard(product)
            productCards.push(card)
        }
        this.loadPage( productCards.join(''))
        this.registerEventForAddingNewCartItem()
    }

    createCard(product){
        const cardTemplate=`
        <div class="col-sm-3">
            <div class="card m-2" style="width: 18rem;">
              <a href="/product/${product.id}">  
              <img src="${product.images}" class="card-img-top" height="250">
              </a>  
              <div class="card-body">
                  <h5 class="card-title">${product.name}</h5>
                  Rp. <h6 class="text-danger d-inline">${product.price}</h6>
                  <p class="card-text">${product.desc}</p>
                  <button type="button" class="btn btn-primary cart-add-item" itemId=${product.id}>Add to cart</button>
                </div>
              </div>
        </div>
        `
        return cardTemplate
    }
   
    registerEventForAddingNewCartItem(){
        const listOfActionButton=document.getElementsByClassName('cart-add-item')

        for (let element of listOfActionButton){
            element.addEventListener('click', function(){
                new Api().addNewItem(this.getAttribute('itemId'))
            })
        }
    }

}
