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
      $t = " Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nulla aperiam quasi minima possimus, minus tenetur error ipsam doloribus laudantium expedita fugit numquam quam eligendi, cupiditate similique? Possimus cum iste culpa.";
      $r = wordwrap($t, 5, "<br/>\n", true);
      echo $r;
    ?>
</div>
</body>
</html>
