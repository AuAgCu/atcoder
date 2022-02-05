<?php
error_reporting(E_ERROR);
fscanf(STDIN, "%d", $n);

$map = array();
for($i = 0; $i < $n-1; $i++) {
    fscanf(STDIN, "%d %d", $a, $b);
    $a--;
    $b--;

    if (!array_key_exists($a, $map)) {
        $map[$a] = array();
    }

    if (!array_key_exists($b, $map)) {
        $map[$b] = array();
    }

    $map[$a][] = $b;
    $map[$b][] = $a;
}

foreach ($map as $k => $v) {
    sort($v);
}

$v = 0;
$flags = array_fill(0, $n-1, false);

recurtion($map, $v, $flags);
echo "\n";

function recurtion($map, $v, $flags) {
    $flags[$v] = true;
    printf("%d ", $v+1);
    foreach ($map[$v] as $i => $w) {
        if ($flags[$w]) {
            continue;
        }
        recurtion($map, $w, $flags);
        printf("%d ", $v+1);
    }
}