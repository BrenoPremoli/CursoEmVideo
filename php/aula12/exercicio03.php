<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="../_css/estilo.css"/>
  <meta charset="UTF-8"/>
  <title>Curso de PHP - CursoemVideo.com</title>
</head>
<body>
<div>
    <form action="exercicio03-1.php" method="get">
        Número <select name="num" >
        <?php
          $c = 1;
          do {
            echo "<option value='$c'>$c</option>";
            $c++;
          } while($c <= 10)
        ?>  
        </select>
        <input type="submit" class="botao" value="Enviar">
    </form>
</body>
</html>
 