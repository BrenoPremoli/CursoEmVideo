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
        function teste(&$x) {
          $x = $x + 2;
          echo "<p>X = $x</p>";
        }
          $a = 3;
          teste($a);
          echo "<p>A = $a</p>";

    ?>
</body>
</html>
 