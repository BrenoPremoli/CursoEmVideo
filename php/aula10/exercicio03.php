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
        $dia = isset($_GET["estado"])?$_GET["estado"]:0;
        switch ($dia) {
          case 1:
          case 13:
          case 3:
          case 20:
          case 21:
          case 25:
          case 4:
            $r = "REGIÃO NORTE";
            break;
          case 2:
          case 5:
          case 26:
          case 9:
          case 14:
          case 16:
          case 17:
          case 18:
          case 24:
            $r = "REGIÃO NORDESTE";
            break;
          case 6:
          case 8:
          case 10:
          case 11:
            $r = "REGIÃO CENTRO-OESTE";
            break;
          case 7:
          case 12:
          case 27:
          case 23:
            $r = "REGIÃO SUDESTE";
            break;
          case 15:
          case 19:
          case 22:
            $r = "REGIÃO SUL";
            break;
        }
        echo "Resultado: $r";
        echo "</br></br>";
    ?>
    <a href="javascript:history.go(-1)" class="botao">Voltar</a>
</body>
</html>
 