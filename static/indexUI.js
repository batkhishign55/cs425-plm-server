
window.addEventListener('load',function(){
    new ApiNotif().callApiCartNotif().then(new UINotif().showCartNotif)
})

class ApiNotif{
    async callApiCartNotif(){
        const resp=await fetch('/cart/api/total-items')
        const jsonresp=await resp.json()
        return jsonresp
    }
}

class UINotif{
    constructor(){
        this.showCartNotif=this.showCartNotif.bind(this)
    }

    showCartNotif(apiresp){
     document.getElementById('notifId').innerHTML=apiresp.data[0].total;        
    }
}
