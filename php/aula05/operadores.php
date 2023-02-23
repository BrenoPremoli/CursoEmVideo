<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="_css/estilo.css">
    <title>operadores</title>
</head>
<body>
    <div>
        <?php
        $n1 = 3;
        $n2 = 2;
        //na url -> http://127.0.0.1:8080/aula05/operadores.php?a=5&b=8 // ?a=5&b=8
        $n1 = $_GET["a"];
        $n2 = $_GET["b"];
        echo "<h2>Valores rebebidos: $n1 e $n2</h2>"; 
        $m = ($n1 + $n2) / 2;
        echo "$n1 + $n2 = ".($n1 + $n2); //soma
        echo "<br>$n1 - $n2 = ".($n1 - $n2); //subtração
        echo "<br>$n1 * $n2 = ".($n1 * $n2); //multiplicação
        echo "<br>$n1 / $n2 = ".($n1 / $n2); //divisão
        echo "<br>$n1 % $n2 = ".($n1 % $n2); //módulo
        echo "<br>Média de $n1 e $n2 = $m"; //módulo
        ?>
    </div>
</body>
</html>