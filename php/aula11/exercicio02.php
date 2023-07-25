<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="../_css/estilo.css"/>
    <meta charset="UTF-8"/>
    <title>Curso de PHP - CursoemVideo.com</title>
</head>
<body>
<div>
    <form action="exercicio02-1.php" method="get">
      <?php
      $c = 1;
      while ($c <= 5)
        {
          echo "Valor $c: <input type='number' name='v$c' min='0' max='100' value='0'/><br>";
          $c++;
        }
        ?>
        <br>
        <input type="submit" class="botao" value="Enviar"/>
    </form>
</div>
</body>
</html>
 