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
        $m=0;
        $n = isset($_GET["num"])?$_GET["num"]:1;
        echo "Múltiplos do número $n: ";
        for ($c = 1; $c <= $n; $c++) {
          if ($n % $c == 0)
          {
            echo "$c ";
            $m++;
          }
        } 
        echo "<br><br>";
        if ($m <= 2)
        {
          echo "É PRIMO";
        }
        else {
          echo "NÃO É PRIMO";
        }
        echo "<br><br>";
        echo "Total de múltiplos: $m";
    ?>
    <br><br>
    <a href="exercicio03.php" class="botao">Voltar</a>
</body>
</html>
 