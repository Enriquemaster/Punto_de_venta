<?php
$dsn = "mysql:host=localhost;dbname=python";
$username = "root";
$password = "Enrique154";

try {
    $pdo = new PDO($dsn, $username, $password);
    // Configurar el manejo de errores
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Conectado exitosamente a MySQL con PDO";
} catch (PDOException $e) {
    echo "Conexión fallida: " . $e->getMessage();
}
?>