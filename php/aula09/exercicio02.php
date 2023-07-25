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
        if($i < 16) {
          $v = "Não Vota";
        }
        elseif (($i >= 16 && $i < 18) || ($i > 65)) {
            $v = "Voto Opcional";
          }
        else {
          $v = "Voto Obrigatório";
        }
        echo "$v";
        echo "</br></br>"
    ?>
    <a href="exercicio02.html">Voltar</a>
</body>
</html>
 