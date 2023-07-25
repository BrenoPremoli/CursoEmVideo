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
        $ano = $_GET["ano"];
        $idade = 2023 - $ano;
        echo "Idade em 2023: $idade";
        $tipo = ($idade >= 18 && $idade < 65) ? "Obrigatório" : "Não obrigatório";
        echo "</br>Voto: $tipo";
    ?>
</div>
</body>
</html>
 