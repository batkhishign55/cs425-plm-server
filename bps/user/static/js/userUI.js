window.addEventListener('load',function(){
    new Api().callApiUser().then(new UI().showUser)

})

class Api{
    async callApiUser(){
        const resp=await fetch(`/user/api/detail`)
        const jsonresp=await resp.json()
        return jsonresp
    }
}

class UI{
    constructor(){
        this.showUser=this.showUser.bind(this)
    }

    showUser(apiresp){
        const getEl=(id)=>document.getElementById(id);
        const user=apiresp.data[0]
        getEl('nickName').innerHTML=user.nickName
        getEl('username').innerHTML=user.username
        getEl('phone').innerHTML=user.phone
        getEl('email').innerHTML=user.email
        getEl('birth').innerHTML=user.birth
        getEl('address').innerHTML=user.address
        getEl('joinedDates').innerHTML=user.joinedDates
        getEl('memberTypes').innerHTML=user.memberTypes
        getEl('profileImage').setAttribute('src', user.images)
    }
 }

