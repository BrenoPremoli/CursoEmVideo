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
      $n = array("A", "J", "M", "X", "K");
      print_r($n);
      //$n[] = "O";
      //array_push($n, "B");
      //array_pop($n);
      //array_unshift($n, "Y");
      //array_shift($n);
      //sort($n);
      //rsort($n);
      //asort($n);
      //arsort($n);
      //print_r($n);
      $n = array(2=>"A", 5=>"J", 3=>"M", 4=>"X", 1=>"K");
      //ksort($n);
      krsort($n);
      print_r($n);
    ?>
  </pre>
</div>
</body>
</html>
