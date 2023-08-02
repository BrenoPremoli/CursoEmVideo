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
      $v = array("nome"=>"ana",
                 "idade"=> "23",
                 "peso"=>"65.5");
      $v["fuma"] = true;
      print_r($v);
      foreach($v as $campo => $valor){
        echo "<br>O valor de $campo é $valor";
      }
    ?>
  </pre>
</div>
</body>
</html>
