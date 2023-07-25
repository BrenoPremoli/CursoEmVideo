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
        $nome = isset($_GET["nome"])?$_GET["nome"]:"[não informado]";
        $ano = isset($_GET["ano"])?$_GET["ano"]:0;
        $sexo = isset($_GET["sexo"])?$_GET["sexo"]:"[indefinido]";
        $idade = date("Y") - $ano;
        echo "Nome: $nome<br/>Idade: $idade<br/>Sexo: $sexo"
    ?>
    <a href="02-exercicio.html">Voltar</a>
</body>
</html>
 