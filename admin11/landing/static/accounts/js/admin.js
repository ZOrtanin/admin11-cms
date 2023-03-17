let btn_order = document.querySelectorAll('.getorder');
let btn_del = document.querySelectorAll('.del');
let modal = document.querySelectorAll('.modal-body');
let csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
let title_modal = document.querySelectorAll('.modal-title')[0];
let form_modal = document.querySelectorAll('.form-edit')[0];
let edit_block = document.querySelectorAll('.edit_block');


edit_block.forEach(item =>{
      item.addEventListener('mouseover', function(){this.querySelectorAll('.setings_block')[0].style.opacity = 1;})
      item.addEventListener('mouseout', function(){this.querySelectorAll('.setings_block')[0].style.opacity = 0.5;})
  });


////////////////////
/// Пост запросы ///
////////////////////

function Post(path,input,func){
      var output = '';
      console.log(csrftoken)
      $.ajax({
          type:'POST',
          url: path,
          data:{
            dataset:input,
            csrfmiddlewaretoken: csrftoken,
          },
          success:function(response){
           console.log('work');
           output = response.responseText; 

          },
          complete:function(response,err){ 
            console.log(response.responseText);
            func(response.responseText);
          },
          error: function(resp){
            //console.log(resp);
            output = resp.responseText;
          }
      })
      console.log(output);
      return output;
}


/////////////////////////
/// работа с заявками ///
/////////////////////////

btn_order.forEach(item =>{
      item.addEventListener('click', selectOrder)
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

btn_del.forEach(item =>{
      item.addEventListener('click', delOrder)
  });

function delOrder(){
	console.log(this.parentElement.parentElement);
      this.parentElement.parentElement.remove()
}


//////////////////////////////
/// кнопка видимости блока ///
//////////////////////////////

let btn_visible = document.querySelectorAll('.button_disable');

btn_visible.forEach(item =>{
      item.addEventListener('click', visibleBlock)
  });

function visibleBlock(){
      let block = this.parentElement.parentElement.parentElement;
      let id_block = this.dataset.id
      let csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

      Post('published/'+id_block+'/')

      if (block.classList.contains('True')){
            block.classList.remove('True');            
            block.classList.add('False');
            this.classList.remove('fa-eye-slash');
            this.classList.add('fa-eye');
      }else{
            block.classList.remove('False');
            block.classList.add('True');
            this.classList.remove('fa-eye');
            this.classList.add('fa-eye-slash');
      }
      console.log(id_block);
}


/////////////////////////
/// Cортировка блоков ///
/////////////////////////

let btn_sort_up = document.querySelectorAll('.button_sort');

btn_sort_up.forEach(item =>{
      item.addEventListener('click', SortBlock)
  });

function SortBlock(){
      var parentElement = document.body; 

      var nodeList = document.querySelectorAll('.edit_block');

      let block = this.parentElement.parentElement.parentElement;

      for (var i = 0; i < nodeList.length; i++){

            nodeList[i].id_element = nodeList[i].classList[1];

            if (block.classList[1] === nodeList[i].classList[1]){

                  if (this.classList[1] === 'button_up'){
                        var theFirstChild = nodeList[i-1];
                  }else{
                        var theFirstChild = nodeList[i+2];
                  }
            }
      }

      var parent = nodeList[0].parentNode;

      parent.insertBefore(block, theFirstChild);

      console.log(nodeList);

      let new_nodelist = document.querySelectorAll('.edit_block');

      output = JSON.stringify(new_nodelist);

      console.log(output);
      Post('/sort/',output);
}


///////////////////////////////
/// Модальное окно настроек ///
///////////////////////////////

var modalSetingsWindow = document.getElementById('ModalSetings');
var modalSetings = new bootstrap.Modal(modalSetingsWindow, {
  keyboard: false
})

let btn_setings = document.querySelectorAll('.button_setings');

btn_setings.forEach(item =>{
      item.addEventListener('click',ShowModal)
  });

function ShowModal(){
      Post('/edit/block/','',OpenWindow);
      console.log('');
}

function OpenWindow(value){
      let content = modalSetingsWindow.querySelectorAll('.modal-body')[0];
      modalSetings.show();

      content.innerHTML = value;

}
