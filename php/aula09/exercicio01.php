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
        $a = isset($_GET["ano"])?$_GET["ano"]:1900;
        $i = date("Y") - $a;
        echo "Ano de Nascimento: $a </br>Idade: $i</br>";
        if($i >= 18) {
          $v = "Vota";
          $d = "Dirige";
        }
        else {
          $v = "Não Vota";
          $d = "Não Dirige";
        }
        echo "$v e $d";
        echo "</br></br>"
    ?>
    <a href="exercicio01.html">Voltar</a>
</body>
</html>
 