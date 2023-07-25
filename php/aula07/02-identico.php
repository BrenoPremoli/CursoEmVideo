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
        $n1 = 3;
        $n2 = "3";
        $r = ($n1 == $n2) ? "SIM" : "NÃO"; #==
        echo "Varíaveis são iguais: $r";
        $r = ($n1 === $n2) ? "SIM" : "NÃO"; #===
        echo "</br>Varíaveis são idênticas: $r";
    ?>
</div>
</body>
</html>
 