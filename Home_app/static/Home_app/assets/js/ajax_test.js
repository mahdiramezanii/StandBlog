function like(slug,id){
    var element=document.getElementById("like")
    $.get('blog/like/${slug}/${id}').then(resposne => {
        if(resposne["response"]==="like"){
            element.className="fa fa-heart"
        }else{
            element.className="fa fa-heart"
        }
    } )
}