<?php
	function get_base_url(&$url){
		$url_parts = parse_url($url);
		return ($url_parts['scheme'] . '://' . $url_parts['host'] . (isset($url_parts['path'])?$url_parts['path']:''));
	}	
	
	if(!isset($argv[1]))
		die('Needs argv[1]');
	$rss = file_get_contents($argv[1]);
	$matches = array();
	preg_match_all('/\<link>([^\<]*)/', $rss,$matches);
	
	foreach($matches[1] as &$url)
		$url = get_base_url($url);
	
	
	echo implode("\n",$matches[1]);
?>