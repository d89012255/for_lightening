<?php

# 檢查檔案是否上傳成功
if ($_FILES['module_file']['error'] === UPLOAD_ERR_OK){
  echo '檔案名稱: ' . $_FILES['module_file']['name'] . '<br/>';
  echo '檔案類型: ' . $_FILES['module_file']['type'] . '<br/>';
  echo '檔案大小: ' . ($_FILES['module_file']['size'] / 1024) . ' KB<br/>';
  echo '暫存名稱: ' . $_FILES['module_file']['tmp_name'] . '<br/>';

  # 檢查檔案是否已經存在
  if (file_exists('upload/' . $_FILES['module_file']['name'])){
    echo '檔案已存在。<br/>';
  } else {
    $file = $_FILES['module_file']['tmp_name'];
    $dest = 'C:/xampp/htdocs/for_lightening/uploads/' . $_FILES['module_file']['name'];

    # 將檔案移至指定位置
    move_uploaded_file($file, $dest);
    $temp = $dest;
    print_r($temp);


  }
} else {
  echo '錯誤代碼：' . $_FILES['module_file']['error'] . '<br/>';
}
if(file_exists($temp)){
  header("Content-type: text/html; charset=utf-8");
  // $in = exec("C:\Users\Danny\AppData\Local\Programs\Python\Python310\python.exe push.py 2>&1", $A, $ret);
  // print_r($A);
  // print_r($ret);
  $answer = shell_exec("./dist/push.exe");
  echo $answer."</br>"; 
}

?>