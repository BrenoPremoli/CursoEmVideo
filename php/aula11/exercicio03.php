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
        $inicio =  isset($_GET["ini"])?$_GET["ini"]:0;
        $final =  isset($_GET["fin"])?$_GET["fin"]:0;
        $incremento =  isset($_GET["inc"])?$_GET["inc"]:1;
        while ($inicio <= $final) {
          echo "$inicio</br>";
          $inicio = $inicio + $incremento;
        }
    ?>
</body>
</html>
 