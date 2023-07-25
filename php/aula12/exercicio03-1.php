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
        $n =  isset($_GET["num"])?$_GET["num"]:1;
        $c = 1;
        do {
          echo "$n X $c = " . $n*$c . "</br>";
          $c++;
        } while($c <= 10)
    ?>
    <br>
    <a href="exercicio03.php" class="botao">Voltar</a>
</body>
</html>
 