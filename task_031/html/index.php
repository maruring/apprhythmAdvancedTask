<?php
$dsn = 'mysql:host=mysql-conteiner;dbname=test';
$user = 'user';
$password = 'passdb';

try {
    $dbh = new PDO($dsn, $user, $password);
    echo "接続成功\n";
} catch (PDOException $e) {
    echo "接続失敗: " . $e->getMessage() . "\n";
    exit(1);
}

$sql = 'SELECT * FROM word';
$sth = $dbh->prepare($sql);
$sth->execute();
$result = $sth->fetchAll(PDO::FETCH_ASSOC);
var_dump($result);