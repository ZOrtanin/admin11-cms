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

try{
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

}catch (error) {
    console.log("Пост запросы")
}


/////////////////////////
/// работа с заявками ///
/////////////////////////

try{

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

}catch (error) {
    console.log("работа с заявками")
}


//////////////////////////////
/// кнопка видимости блока ///
//////////////////////////////

try{
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

}catch (error) {
    console.log("кнопка видимости блока")
}


/////////////////////////
/// Cортировка блоков ///
/////////////////////////

try{
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

}catch (error) {
    console.log("Cортировка блоков")
}

/////////////////////////////
/// Кнопка удаления блока ///
/////////////////////////////

try{
    let btn_del_block = document.querySelectorAll('.button_del');

    btn_del_block.forEach(item =>{
          item.addEventListener('click', DelBlock)
      });

    function DelBlock(){
          let isBoss = confirm("Вы уверенны что хотите удалить?");
          if ( isBoss ){ // true, если нажата OK

                console.log(this.dataset.id);
                Post('del/'+this.dataset.id+'/');
                let block = this.parentElement.parentElement.parentElement;
                block.remove();
          }
    }

}catch (error) {
    console.log("Кнопка удаления блока")
}

////////////////////////////////////////
/// Модальное окно добовление блоков ///
////////////////////////////////////////

let buttons_AddTypeBlock = document.querySelectorAll('.button_AddTypeBlock');
let input_name = document.getElementsByName('NameBlock')[0];

try{

    

    input_name.addEventListener('input', ctrlButton, false);

    function ctrlButton() {
          // 
          buttons_AddTypeBlock.forEach(item =>{ 
                console.log("work");     
                item.disabled = this.value.trim().length === 0;
          });  
    }

    buttons_AddTypeBlock.forEach(item =>{      
          item.addEventListener('click',AddTypeBlock)
      });

    function AddTypeBlock(event){
          //event.preventDefault();
          let input = document.getElementsByName("TypeBlock")[0];
          input.value = this.dataset.type

    }

}catch (error) {
    console.log("Модальное окно добовление блоков")
}


///////////////////////////////
/// Модальное окно настроек ///
///////////////////////////////

try{

    var modalSetingsWindow = document.getElementById('ModalSetings');
    var modalSetings = new bootstrap.Modal(modalSetingsWindow, {
      keyboard: false
    })

    let btn_setings = document.querySelectorAll('.button_setings');

    btn_setings.forEach(item =>{
          item.addEventListener('click',ShowModal);
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

        add_button_button(content);
        AddFilePath(content);
    }

    // Кнопка добовления картинок
    let url_file = '';
    let input_file = '';

    function AddFilePath(content){
        let buttons = content.querySelectorAll('.add-file-base');

        console.log('work1');

        buttons.forEach( item => {
            console.log('work1');
            item.addEventListener('click',function (){
                Post('/files/get_files/','',RenderFiles);
                input_file = item.nextElementSibling
                console.log(item.nextElementSibling)
            });
        });
    }

    function RenderFiles(value){
        let modal = document.getElementById('ModalFiles');
        let content = modal.querySelectorAll('.modal-body')[0];
        content.innerHTML = value;

        let div = content.querySelectorAll('.files-upload');
        div.forEach( item => {
            console.log('work1');
            item.addEventListener('click',function (){
              
              let image = item.querySelectorAll('img')[0];
              console.log(image.getAttribute('src'));
              input_file.value = image.getAttribute('src');
                //Post('/files/get_files/','',RenderFiles);
            });
        });

    }



    // Сохронение данных
    let btn_test = document.querySelectorAll('.button_save_test')[0];

    //let btn_test = document.querySelectorAll('.btnSubmitsForm')[0];

    btn_test.addEventListener('click',SaveSettings)

    function SaveSettings(event){
          //event.preventDefault();
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

}catch (error) {
    console.log("Модальное окно настроек")
}

///////////////////////
/// Загрузка файлов ///
///////////////////////

try{

    const fileDropzone = document.getElementById('file-dropzone');
    const fileInput = document.getElementById('file-input');
    const removeButton = document.getElementById('remove-files');
    const form = document.getElementById('upload-form');
    const selectedFilesDiv = document.getElementById('selected-files');
    const fileInputButton = document.getElementById('file-input-button');

    //const fileInput = document.getElementById('file-input');
    //const fileInputButton = document.getElementById('file-input-button');
    const selectedFilesContainer = document.getElementById('selected-files');

    // Отображаем выбранные файлы перед загрузкой
    fileInput.addEventListener('change', () => {
      
      const files = Array.from(fileInput.files);
      render_files(files);
      
    });

    function render_files(files){
        const selectedFilesContainer = document.getElementById('selected-files');
        selectedFilesContainer.innerHTML = '';

        files.forEach(file => {

            const fileItem = document.createElement('div');                            
            fileItem.classList.add('file-item');

            const filePreview = document.createElement('img');
            filePreview.classList.add('file-preview');

            const removeFileButton = document.createElement('button');
            removeFileButton.classList.add('remove-file-button');
            removeFileButton.innerHTML = '<i class="fa-solid fa-xmark"></i>';

            removeFileButton.addEventListener('click', () => {
              fileItem.remove();
              fileInput.files = fileInput.files.filter(f => f !== file);
            });

            const reader = new FileReader();

            reader.onload = () => {
              filePreview.src = reader.result;
            }

            reader.readAsDataURL(file);
            fileItem.appendChild(filePreview);
            fileItem.appendChild(removeFileButton);
            selectedFilesContainer.appendChild(fileItem);
      });
    }

    // Выбор файлов через кнопку
    fileInputButton.addEventListener('click', () => {
      fileInput.click();
    });

    // Обрабатываем перетаскивание файлов
    fileDropzone.addEventListener('dragover', (event) => {
        event.preventDefault();
        fileDropzone.classList.add('dragging');
    });

    fileDropzone.addEventListener('dragleave', () => {
        fileDropzone.classList.remove('dragging');
    });


    fileDropzone.addEventListener('drop', (event) => {
      event.preventDefault();
      fileDropzone.classList.remove('dragging');
      const files = Array.from(event.dataTransfer.files);
      render_files(files);
      fileInput.files = new DataTransfer().files;
      const dataTransfer = new DataTransfer();
      files.forEach(file => {
        dataTransfer.items.add(file);
        //fileInput.files.add(file);
      });
      fileInput.files = dataTransfer.files;
    });
    // fileDropzone.addEventListener('drop', (event) => {
    //     event.preventDefault();
    //     fileDropzone.classList.remove('dragging');
    //     const files = Array.from(event.dataTransfer.files);
    //     //showSelectedFiles(files);

    //     console.log(fileInput)        
    //     render_files(files);

    //     fileInput.files = new DataTransfer().files;
    //     files.forEach(file => {
    //         console.log('+++');
    //         fileInput.files.add(file);
    //     });

        // const newFiles = Object.create(FileList.prototype);
        // newFiles.length = 0;

        // files.forEach(file => {
        //     console.log('+++');
        //     newFiles[newFiles.length++] = file;
        // });

        // fileInput.files = newFiles;

    //});

    // Детали картинки
    let buttonsDetail_my = document.querySelectorAll('.button-detail');

    console.log(buttonsDetail_my);

    buttonsDetail_my.forEach( item => {    
        item.addEventListener('click', () => {
            console.log(item.dataset.id);
            Post('get_file/'+item.dataset.id+'/','',PrintModalImage)
        });
    });

    function PrintModalImage(data){
        let modal = document.getElementById('DetailModal');

        let block_info = modal.querySelector('.modal-body');

        block_info.innerHTML = data;

    }



}catch (error) {
    console.log("Загрузка файлов")
}





