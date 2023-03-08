// модал заказы

let btn_order = document.querySelectorAll('.getorder');
let btn_del = document.querySelectorAll('.del');
let csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
let modal = document.querySelectorAll('.modal-body');
let title_modal = document.querySelectorAll('.modal-title')[0];

let form_modal = document.querySelectorAll('.form-edit')[0];


btn_order.forEach(item =>{
      item.addEventListener('click', selectOrder)
  });

btn_del.forEach(item =>{
      item.addEventListener('click', delOrder)
  });

function selectOrder () {
      //this.parentElement.classList.toggle('select-active');
	console.log(this.dataset.idOrder);

	let order = this.dataset.idOrder;

	$.ajax({
    type:'POST',
    url: this.dataset.path,
    data:{
      csrfmiddlewaretoken: csrftoken,
    },
    success:function(response){
     console.log('work');         
    },
    complete:function(response,err){
    	title_modal.innerHTML = 'Заказ №' + order;
    	modal[0].innerHTML = response.responseText;
    	form_modal.action = '/orders/edit/'+order+'/'
    	console.log(response.responseText);

 	},
    error: function(resp){
      console.log(resp);
    }
  })
}

function delOrder(){
	
}