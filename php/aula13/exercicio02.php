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
        Número <select name="num" >
        <?php
          for ($c = 1; $c <= 10; $c++) {
            echo "<option value='$c'>$c</option>";
          }
        ?>  
        </select>
        <input type="submit" class="botao" value="Enviar">
    </form>
</body>
</html>
 