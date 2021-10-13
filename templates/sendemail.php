<?php
error_reporting(E_ALL);
$to = "info@sharanyadham.com, sharanyadham@gmail.com";
$subject = "Contact Us Form Submitted";

$message = '
<html>
<head>
<title>HTML email</title>
</head>
<body>
<table>
<tr>
<th>Name</th>
<th>'.$_POST['name'].'</th>
</tr><tr>
<th>Email</th>
<th>'.$_POST['email'].'</th>
</tr><tr>
<th>Contact</th>
<th>'.$_POST['phone'].'</th>
</tr><tr>
<th>Message</th>
<th>'.$_POST['message'].'</th>
</tr>
</table>
</body>
</html>
';

// Always set content-type when sending HTML email
$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

// More headers
$headers .= 'From: <info@sharanyadham.com>' . "\r\n";



if($_POST['name'] != '' && $_POST['email'] != ''){


  mail($to,$subject,$message,$headers);
  header("location: /thankyou.html");
} else {
  header("location: /");
}
?>