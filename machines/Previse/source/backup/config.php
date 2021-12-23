<?php

function connectDB(){
    $host = 'localhost';
    $user = 'root';
    $passwd = 'mySQL_p@ssw0rd!:)';
    $db = 'previse';
    $mycon = new mysqli($host, $user, $passwd, $db);
    return $mycon;

    // o day neu no taoj duoc reverse-shell ung dung, ma chua du quyen de vao sau he thong, ma ung dung dang chay mysql thi no co the lay thong tin username, password de dang nhap vao db cua ung dung vay la xong cmn roi 
}

?>
