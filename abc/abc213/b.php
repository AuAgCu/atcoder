<?php
fscanf(STDIN, "%d", $n);
$arr = explode(" ", fgets(STDIN));
$map = array();
foreach ($arr as $i => $v) {
    $map += array($v => $i+1);
}

krsort($map);
echo array_values($map)[1];