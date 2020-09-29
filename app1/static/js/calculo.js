var op1, op2;
var varOperador;

function operador (idd) {
   op1 = document.getElementById('visor').innerHTML;
   switch (idd) {
       case "soma":
           varOperador = "+";
           break;
       case "subtracao":
           varOperador = "-";
           break;
       case "multiplicacao":
           varOperador = "*";
           break;
       case "divisao":
           varOperador = "/";
           break;         
   }
   document.getElementById("visor").innerHTML = varOperador;
}

function resultado() {
    if (op1!=undefined) {
            op2 = document.getElementById('visor').innerHTML;
            op1 = parseFloat(op1)
            op2 = parseFloat(op2)

            switch (varOperador) {
                case "+":
                    r = op1 + op2;
                    break;
                case "-":
                    r = op1 - op2;
                    break;
                case "/":
                    r = op1 / op2;
                    break;
                case "*":
                    r = op1 * op2;
                    break;        
            }

                if (op2==0 && varOperador=="/") {
                     alert("Desculpe, numero indivisivel por 0!")
                     document.getElementById("visor").innerHTML = "0"
                }  else {
                    if (r%1 != 0) {
                        r = r.toPrecision(8)
                    }
                    document.getElementById("visor").innerHTML = r;
                }
                  
                 op1 = undefined;
                 op2 = undefined;
                 varOperador = undefined;
    }
}

    function btponto() {
        document.getElementById('visor').innerHTML += ".";
    }

  function maisEmenos() {
      visoratual = document.getElementById("visor").innerHTML
        if (visoratual == "0" || visoratual == "+" || visoratual == "-" || visoratual == "/" || visoratual == "*") {
            return;
        } else {
            if (visoratual.search("-") == -1) {
                document.getElementById("visor").innerHTML = "-" + visoratual;
            } else {
                document.getElementById("visor").innerHTML = visoratual.substring(1);
            }
        }
  } 


     function botnumero(idd) {
         botao = document.getElementById(idd).innerHTML
         visoratual = document.getElementById("visor").innerHTML
            if (visoratual == "0" || visoratual == "+" || visoratual == "-" || visoratual == "/" || visoratual == "*") {
                document.getElementById("visor").innerHTML = botao;
            } else {
                if (visoratual.length >= 10) {
                    return;
                } else {
                    document.getElementById("visor").innerHTML += botao;
                }
            }
     }

  function btlimpar() {
      document.getElementById("visor").innerHTML = 0;
      op1 = undefined;
      op2 = undefined;
      varOperador = undefined;
  } 

    