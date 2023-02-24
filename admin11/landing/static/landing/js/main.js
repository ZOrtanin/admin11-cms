const navLinks = document.querySelectorAll('.nav-item');
const menuToggle = document.getElementById('offcanvasNavbar');
// //const bsCollapse = new bootstrap.Collapse(menuToggle, {toggle:false})
const bsOffcanvas = new bootstrap.Offcanvas(menuToggle, {toggle:false});

navLinks.forEach((l) => {
  
     l.addEventListener('click', () => { bsOffcanvas.hide() });
    // console.log(menuToggle);
    // let bgarr = document.querySelectorAll('.offcanvas-backdrop');
    // bgarr[0].remove();
})


// кнопка навигации по странице

var body = document.body,html = document.documentElement;

var heightPage = Math.max( body.scrollHeight, body.offsetHeight, 
                 html.clientHeight, html.scrollHeight, html.offsetHeight );


const BtnNav = document.getElementById('BtnUpTop');

let opacity = 0

BtnNav.style.cssText = 'opacity:0;';

// подключаем анимацию к js
var an_revolver = document.getElementById('p1');
let flag_an = true;

// вешаем слушателя для остоновки анимации
an_revolver.addEventListener('beginEvent', (event) => { 
  flag_an = false;
});


window.addEventListener('scroll', function() {
  //console.log(pageYOffset + 'px');

  // Скрываем кнопку и показываем 
  if (pageYOffset > 400){
    
    BtnNav.classList.remove("scroll-hide");

    if (opacity == 0){
      fadeIn(BtnNav, 300);
      opacity = 1;
    }          

  }else{

    if (opacity == 1){            
      fadeOut(BtnNav, 300);
      opacity = 0;
    }
    
  }

  // Запускаем анимацию обводки при появлении на экране
  //console.log(pageYOffset);
  //console.log(pageYOffset/(document.body.scrollHeight/100));
  if (pageYOffset/(document.body.scrollHeight/100) > 43 && flag_an == true ){          
    an_revolver.beginElement();         
  }

  // Рисуем градиент 
  var out = pageYOffset/(heightPage/100)
  BtnNav.children[0].style.cssText = 'background: linear-gradient( #fff '+ out+'% , rgb(255, 193, 7) '+ out+'%) !important';

}); 


// Функция для появлениея любого элемента
function fadeIn(el, speed) {
  var step = 1 / speed;
  var interval = setInterval(function() {
    if (+el.style.opacity >= 1)
      clearInterval(interval);
      
    el.style.opacity = +el.style.opacity + step;
  }, speed / 1000);
}

// Функция для исщезновения любого элемента
function fadeOut(el, speed) {
  var step = 1 / speed;
  var interval = setInterval(function() {
    if (el.style.opacity <= 0)
      clearInterval(interval);
      
    el.style.opacity = el.style.opacity - step;
  }, speed / 1000);
}

// Переключаем табы 4х причин
let mouse_off = false;
var pole_stop = document.getElementById('mouse_muve');
let currentElem = null;

pole_stop.onmouseover = function(event) {
  if (currentElem) return;
  
  let target = event.target.closest('div');

  currentElem = target;

  // console.log("вход");
  mouse_off = true;
};

pole_stop.onmouseout = function(event) {
  if (!currentElem) return;
  let relatedTarget = event.relatedTarget;        

  while (relatedTarget) {
    if (relatedTarget == currentElem) return;
    relatedTarget = relatedTarget.parentNode;
  } 

  currentElem = null;

  // console.log("выход");
  mouse_off = false;
};


function slide(speed){
  var step = 1;
  var interval = setInterval(function(){
    
    if (mouse_off == false){
      var firstTabEl = document.querySelector('#pills-tab li:nth-child('+step+') button');
      var firstTab = new bootstrap.Tab(firstTabEl).show();
    }

    if (step == 4 ){
      step = 0;
    }    
    
    step = step + 1;    
    
  }, speed / 1000);
}
slide(3000000);


// ----------------- Калькулятор ---------------------------
// Инпуты
let comps = document.getElementById('comps');
let servers = document.getElementById('servers');

// Кнопки
let btnAddComp = document.getElementById('add_comp');
let btnRmvComp = document.getElementById('rmv_comp');
let btnAddServer = document.getElementById('add_server');
let btnRmvServer = document.getElementById('rmv_server');

// Цены
let optimum = document.getElementById('price-opt');
let maximum = document.getElementById('price-max');

// Время
let timework = document.getElementById('time-work');

function adder(event){
  event.preventDefault();
  let input = this.parentNode.querySelectorAll('input')[0];
  let number = Number(input.value);

  number = number + 1;
  input.value = number; 
  addPricing();   
}

function rmver(event){
  event.preventDefault();
  let input = this.parentNode.querySelectorAll('input')[0];
  let number = Number(input.value);

  if (number > 0){
    number = number - 1;
    input.value = number;
  }
  addPricing();
}

function addPricing(){

  timework.innerHTML=( Number(comps.value)*0.5 )+( Number(servers.value)*1 );

  optimum.innerHTML=( Number(comps.value)*2000 )+( Number(servers.value)*6000 );
  maximum.innerHTML=( Number(comps.value)*3000 )+( Number(servers.value)*6000 );

}

addPricing();

btnAddComp.addEventListener("click", adder);
btnAddServer.addEventListener("click", adder);

btnRmvComp.addEventListener("click", rmver);
btnRmvServer.addEventListener("click",rmver);


// -------------------- Модальные окна ------------------

let btnMaximum = document.getElementById('btnMaximum');
let btnOptimum = document.getElementById('btnOptimum');
let btnStandart = document.getElementById('btnStandart');

let modalLable = document.querySelectorAll('.ModalLabel')[0];
let modalPrice = document.getElementById('price_tarif');

function newLable(event){
  console.log(comps.value);
  console.log(servers.value);
  price = this.parentNode.getElementsByTagName('f')[0].innerHTML;

  if (typeof this.parentNode.getElementsByTagName('f')[1] !== 'undefined') {
    time = this.parentNode.getElementsByTagName('f')[1].innerHTML;
  }else{
    time = '';
  }
  console.log(modalLable);
  modalLable.innerHTML=this.dataset.mytitle;
  modalPrice.value="Тариф: "+this.dataset.tarif+"\nКомпьютеров: "+comps.value+"\nСерверов: "+servers.value+"\nЦена: "+price+"\nВремя: "+time+"\n------------\n\n";
}

btnStandart.addEventListener("click", newLable);
btnOptimum.addEventListener("click", newLable);
btnMaximum.addEventListener("click", newLable);



// -------------------- Отправка форм -------------------

let btnSubmits = document.querySelectorAll('.btnSubmits');

function sendForm(event){
  event.preventDefault();
  let form = this.parentNode.parentNode;
  let url_post = form.attributes['action'].value;
  console.log(form.name.value);
  let err = [];

  $.ajax({
    type:'POST',
    url: url_post,
    data:{
      csrfmiddlewaretoken: form.csrfmiddlewaretoken.value,
      name: form.name.value, 
      telephone: form.telephone.value,
      message: modalPrice.value+form.message.value,
      form_name: form.form_name.value
    },
    success:function(response){
     console.log('work');         
    },
    complete:function(response,err){
     console.log(response.responseText);

     if (response.responseText=='Cообщение отправленно'){
       $('#Modal').modal('hide');
       form.name.value = '';
       form.telephone.value = '';
       modalPrice.value = '';
       form.message.value='';
       form.form_name.value='';

       console.log(form.elements);

       $('#AlertsMessage').html('Сообщение отправленно');
       $('#ModalAlerts').modal('show');

       for (let i = 0; i < form.elements.length; i++) {
        console.log(form.elements[i]); 
          if (form.elements[i].nodeName === "INPUT") {    
            form.elements[i].style.cssText += 'background-color:#fff';
          }
        }

     }else{
      console.log(response.responseText);
      err = response.responseText.split('/');

      $('#AlertsMessage').html('Не все поля заполнены!');
      // $('#ModalAlerts').modal({
      //   focus:true,
      //   show:true
      // });
      $('#ModalAlerts').modal('show');

      err.forEach((l) => {      
        //console.log();
        form[l].style.cssText += 'background-color:#ffc107';
      })

      

     }
    },
    error: function(resp){
      console.log(resp);
    }

  })


}

//btnSubmits.addEventListener("click", sendForm);

btnSubmits.forEach((l) => {  
     l.addEventListener('click', sendForm);  
})

