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
        function soma($a, $b) {
          return $a + $b;
        }

          $x = 5;
          $y = 4;
          $r = soma($x, $y);
          echo "A soma vale $r";

    ?>
</body>
</html>
 