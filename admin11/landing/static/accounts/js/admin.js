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
            //console.log(response.responseText);
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
      let id_block = this.dataset.id;
      let form = modalSetingsWindow.querySelectorAll('.FormSettings')[0];
      
      console.log(id_block);
      form.action = "save/"+id_block+"/";
      Post('/edit/block/'+id_block+'/','',OpenWindow);
      console.log('');
}

function OpenWindow(value){
      let content = modalSetingsWindow.querySelectorAll('.modal-body')[0];

      modalSetings.show();
      content.innerHTML = value;
      //console.log(value)
      //arr = ['.menu-admin','social_link-admin']

      add_button_button(content)
}

// Сохронение данных
let btn_test = document.querySelectorAll('.button_save_test')[0];

//let btn_test = document.querySelectorAll('.btnSubmitsForm')[0];

btn_test.addEventListener('click',SaveSettings)

function SaveSettings(){
      console.log("Работает");
      let form = modalSetingsWindow.querySelectorAll('.FormSettings')[0];
      
      let inputs = form.querySelectorAll('input');
      inputs.forEach(item =>{
            //console.log(item.value);
            item.setAttribute('value', item.value);
      });

      let textarea = form.querySelectorAll('textarea');
      textarea.forEach(item =>{
            //console.log(item.value);
            item.innerHTML = item.value;
      });


      let html = form.querySelectorAll('.content_admin')[0];



      let out = document.getElementsByName("content_admin")[0];
      
      out.value = html.innerHTML;

      //console.log(inputs);
}

function TestSaveSettings(){
      //document.getElementById('my-form').addEventListener('submit', function(event) {
      // Отменяем стандартное действие браузера по отправке формы
      //event.preventDefault();
      let form = modalSetingsWindow.querySelectorAll('.FormSettings')[0].querySelectorAll('.content_admin')[0];


      // Создаем объект для хранения данных формы
      var formData = {};

      // Получаем значения полей формы и добавляем их в объект
      var inputs = form.querySelectorAll('input');
      for (var i = 0; i < inputs.length; i++) {
            formData[inputs[i].name] = inputs[i].value;
      }

      try{
            var textarea = form.querySelector('textarea');
            formData[textarea.name] = textarea.value;
      }catch{}

      // Создаем объект для хранения кнопки
      // formData['Button'] = {
      //     'link': form.querySelector('input[name="link"]').value,
      //     'label': form.querySelector('input[name="label"]').value
      // };

      // form.forEach((item) => {
      //   const label = item.querySelector('.label').value;
      //   const link = item.querySelector('.link').value;
      //   formData['Button'].push({ label, link });
      // });

      // Создаем JSON-строку из объекта
      var json = JSON.stringify(formData);

      // Выводим результат в консоль
      console.log(json);
      //});
}


// Добовление кнопки нового элемента
function add_button_button(content){      
      let block_menu = content.querySelectorAll('.add_block');
      let button = '<div class="col-3 ms-1 d-flex justify-content-center align-items-center"><button class="add_block_button btn btn-primary">Добавить +</button></div>';

      block_menu.forEach(item =>{            
            item.insertAdjacentHTML("beforeEnd", button);
      });

      let block_item = content.querySelectorAll('.item');
      let button_close = '<div class="del_block btn btn-primary">X</div>';


      block_item.forEach((item,index) =>{
            // console.log(index);
            // console.log(item.parentElement.classList.contains('add_block')) 
            if(item.parentElement.classList.contains('add_block')){
                  item.insertAdjacentHTML("afterBegin", button_close);
            }           
            
      });
      

      // block_menu.appendChild(div)
      console.log(block_menu); 
      add_block_button();
      del_buttons_adding();     

}


// удаление блоков
function del_block_item(event){
      event.preventDefault();
      
      parent = this.parentElement.parentElement.querySelectorAll('.item');;
      console.log(parent.length);
      if(parent.length >= 2){
            this.parentElement.remove()
      }else{
            alert("Один элемент всегда должен остоваться!")
      }
}

function del_buttons_adding(){
      let buttons = document.querySelectorAll('.del_block');

      buttons.forEach(item =>{            
            item.addEventListener('click',del_block_item)
      });
}


// добовление блоков
function add_block_button(){
      let buttons = document.querySelectorAll('.add_block_button');

      buttons.forEach(item =>{            
            item.addEventListener('click',add_block_item)
      });
}

function add_block_item(event){
      event.preventDefault();
      
      let parent = this.parentElement.parentElement
      let new_block = this.parentElement.previousElementSibling.cloneNode(true);

      let new_input = new_block.querySelectorAll('input');

      new_input.forEach(item =>{
            console.log('work');
            console.log(item)
            item.setAttribute('value', '');
      });



      //parent.append(new_block);
      this.parentElement.insertAdjacentElement('beforeBegin', new_block);
      console.log(parent)
      del_buttons_adding();
}


// <div class="col-3 ms-1" name="item" style="background-color:rgb(218, 230, 237);padding:5px ; border-radius: 9px; margin-bottom: 10px;">
// <div name="label" class="mb-3">
// <label class="col-form-label" for="id_name">label:</label>
// <input class="form-control" type="text" name="label-menu" value="Контакты2">
// </div>
// <div name="link" class="mb-3">
// <label class="col-form-label" for="id_name">link:</label>
// <input class="form-control" type="text" name="link-menu" value="#contacts">
// </div>
// </div>








