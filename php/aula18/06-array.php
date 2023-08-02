<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="../_css/estilo.css"/>
  <meta charset="UTF-8"/>
  <title>Curso de PHP - CursoemVideo.com</title>
</head>
<body>
<div>
  <pre>
    <?php
      $n = array(array(2,3),
                 array(3,4),
                 array(9,5));
      $n[0][1]=$n[2][0];
      print_r($n);
    ?>
  </pre>
</div>
</body>
</html>
