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
        $v = isset($_GET["val"])?$_GET["val"]:1;
        echo "<h2>FATORIAL DE: $v!<br></h2>";
        $c = $v;
        $fat = 1;
        do {
          $fat = $fat * $c;
          $c--;
        } while($c >= 1);
        echo "<h3>Resultado: $fat<br></h3>";
      ?>
        <br>
        <a href="exercicio02.html" class="botao">Voltar</a>
</div>
</body>
</html>
 