<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="../_css/estilo.css"/>
  <meta charset="UTF-8"/>
  <title>Curso de PHP - CursoemVideo.com</title>
</head>
<body>
<div>
    <?php
        $n1 = isset($_GET["n1"])?$_GET["n1"]:0;
        $n2 = isset($_GET["n2"])?$_GET["n2"]:0;
        $m = ($n1 + $n2) / 2;
        echo "Nota 1: $n1 </br>Nota 2: $n2</br>Média: $m<br/>";
        if($m < 5) {
          $r = "REPROVADO";
        }
        elseif ($m >= 5 && $m <= 7) {
            $r = "EM RECUPERAÇÃO";
        }
        else {
        $r = "APROVADO";
        }
        echo "Situação: $r";
        echo "</br></br>"
    ?>
    <a href="exercicio03.html">Voltar</a>
</body>
</html>
 