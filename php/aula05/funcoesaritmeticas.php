<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="_css/estilo.css">
    <title>funcoes aritmeticas</title>
    <style>
        h2 {
            font: 15pt Arial;
            color: #171560;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div>
        <?php
        $v1 = $_GET["x"];
        $v2 = $_GET["y"];
        echo "<h2>Valores recebidos: $v1 e $v2</h2>";
        echo "Valor absoluto de $v2 = ". abs($v2);
        echo "<br>$v1<sup>$v2</sup> = ". pow($v1, $v2);
        echo "<br>Raiz Quadrada de $v1 = ". sqrt($v1);
        echo "<br>Valor arredondado de $v2 = ". round($v2); // ceil -> arredonda pra cima // floor -> arredonda pra baixo
        echo "<br> Parte inteira de $v2 = ". intval($v2);
        echo "<br> $v1 em moeda = R$" . number_format($v1, 2, ",",".")
        ?>
    </div>
</body>
</html>