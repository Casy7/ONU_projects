<!DOCTYPE HTML>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta charset="utf-8">
	<title>brain catalog grabing</title>
</head>
	<body>

	<?php
	$context = stream_context_create([
        'http' => 
        [
			'method' => 'POST',
			'header'  => 'Content-type: application/x-www-form-urlencoded',
            'content' => http_build_query
            (
                [
				'login' => 'casy@zest.com.ua',
				'password' => 'b6f19093a07cdf6e2fe098d7aee90b2f'
                ]
            )
		]
	]);
	$sid = substr(file_get_contents('http://api.brain.com.ua/auth', false, $context),22,26);
	echo file_get_contents('http://api.brain.com.ua/product_options/'.'тут_пиши_код_товара'.'/'.$sid);
	?>

	</body>
</html>
