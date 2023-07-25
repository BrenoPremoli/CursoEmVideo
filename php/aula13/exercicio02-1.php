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
        $n = isset($_GET["num"])?$_GET["num"]:1;
        for ($c = 1; $c <= 10; $c++) {
          echo "$n X $c = " . $n*$c . "</br>";
        } 
    ?>
    <br>
    <a href="exercicio02.php" class="botao">Voltar</a>
</body>
</html>
 