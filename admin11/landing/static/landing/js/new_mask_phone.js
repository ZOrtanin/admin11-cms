/*
 ------------------------------------------------------------------------
 * Name             : New mask hpone
 * Author           : Егор Кукольщиков
 * Version          : 1.0.0                                            
 * Created          : 22.10.21
 * File Description : https://t.me/Worker_money2021 если че писать сюда
 * Tutorial         : https://youtu.be/Lxj_v5z0xRE
 * Сountry          : rus, tur
 *-----------------------------------------------------------------------
 */

document.addEventListener("DOMContentLoaded",function(){

  //console.log("Привет");

  let phtoneinputs = document.querySelectorAll('input[data-tel-input]');
  //console.log(phtoneinputs); 

  let getInputNumberValue = function(input){
    return input.value.replace(/\D/g,"");
  }

  let onMyKeyDownInput = function(e){
    //console.log('keyDown');
    let input = e.target,
        inputNumbersValue = getInputNumberValue(input),
        selectionStart = input.selectionStart,
        formattedInputValue = input.value;  


    if (e.inputType == "deleteContentBackward" &&  formattedInputValue.substr(formattedInputValue.length-1) == '-'){
       formattedInputValue = formattedInputValue.substr(0,formattedInputValue.length-1)
    }

    if (e.inputType == "deleteContentBackward" &&  formattedInputValue.substr(formattedInputValue.length-1) == ' '){
       formattedInputValue = formattedInputValue.substr(0,formattedInputValue.length-1)
    }

    if (e.inputType == "deleteContentBackward" &&  formattedInputValue.substr(formattedInputValue.length-1) == '('){
       formattedInputValue = "";
    }
    input.value = formattedInputValue;
    return formattedInputValue;
  }

  let onPhoneKeyDownInput = function(e){
    //console.log('keyDown');
    let input = e.target,
        inputNumbersValue = getInputNumberValue(input),
        selectionStart = input.selectionStart,
        formattedInputValue = input.value;
   
    if (e.key == "Backspace" &&  formattedInputValue.substr(formattedInputValue.length-1) == '-'){
       //console.log('<-');
       formattedInputValue = formattedInputValue.substr(0,formattedInputValue.length-1)
    }

    if (e.key == "Backspace" &&  formattedInputValue.substr(formattedInputValue.length-1) == ' '){
       //console.log('<-');
       formattedInputValue = formattedInputValue.substr(0,formattedInputValue.length-1)
    }

    if (e.key == "Backspace" &&  formattedInputValue.substr(formattedInputValue.length-1) == '('){
       //console.log('<-');
       formattedInputValue = "";
    }

    input.value = formattedInputValue;
    return formattedInputValue;
  }

  let onPhoneInput = function(e){    
    let input = e.target,
        inputNumbersValue = getInputNumberValue(input),
        selectionStart = input.selectionStart,
        formattedInputValue = "";

    if (!inputNumbersValue){
      return input.value='';
    }



    if (["7","8"].indexOf(inputNumbersValue[0])>-1){
      // russian number

      //if (inputNumbersValue == "9") inputNumbersValue = "7"+ inputNumbersValue; 
      let firstSymbol = (inputNumbersValue[0] == "8") ? "8" : "+7";

      formattedInputValue = firstSymbol + " ";

      if (inputNumbersValue.length > 1){
        formattedInputValue += "(" + inputNumbersValue.substring(1,4);
      }

      if (inputNumbersValue.length > 4){
        formattedInputValue += ") " + inputNumbersValue.substring(4,7);
      }

      if (inputNumbersValue.length > 7){
        formattedInputValue += '-' + inputNumbersValue.substring(7,9);
      }

      if (inputNumbersValue.length >= 9){
        formattedInputValue += '-' + inputNumbersValue.substring(9,12);
      } 

    }else{
      // not russian number

      formattedInputValue = "+" + inputNumbersValue.substring(0,16);
      //console.log(formattedInputValue.substr(0,3));

      if (formattedInputValue.substr(0,3) == '+90'){
        formattedInputValue = formattedInputValue.substr(0,3) + " (";

        if (inputNumbersValue.length > 2){
          formattedInputValue += inputNumbersValue.substring(2,5);
        }
        if (inputNumbersValue.length > 5){
          formattedInputValue += ") ";
          formattedInputValue += inputNumbersValue.substring(5,16);
        }
      }
    } 

    if (input.value.length != selectionStart){      
      if(e.data && /\D/g.test(e.data)){
        mynewstr = input.value.substr(0,input.selectionStart-1);        
        input.value = mynewstr + input.value.substr(input.selectionStart);
        input.selectionStart = selectionStart-1;
        input.selectionEnd = selectionStart-1;        
      }
      return;
    }

    input.value = formattedInputValue;
    return formattedInputValue;      
  }

  for(i=0;i<phtoneinputs.length; i++){
    let input = phtoneinputs[i];
    input.addEventListener("input",onPhoneInput);
    input.addEventListener("keydown",onPhoneKeyDownInput);
    //input.addEventListener("input",onMyKeyDownInput);
  }
}); 