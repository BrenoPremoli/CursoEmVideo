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
        $dia = isset($_GET["ds"])?$_GET["ds"]:0;
        switch ($dia) {
          case 2:
          case 3:
          case 4:
          case 5:
          case 6:
            $r = "Tem Aula";
            break;
          case 7:
          case 8:
            $r = "Não tem Aula";
            break;
          default:
            $r = "Dia inválido!";
            break;
        }
        echo "Resultado: $r";
        echo "</br></br>";
    ?>
    <a href="javascript:history.go(-1)" class="botao">Voltar</a>
</body>
</html>
 