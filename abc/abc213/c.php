<?php
error_reporting(E_ERROR);

fscanf(STDIN, "%d %d %d", $h, $w, $n);
$aArr = array();
$bArr = array();
$xyArr = array();
for ($i = 0; $i < $n; $i++) {
    fscanf(STDIN, "%d %d", $a, $b);
    $aArr[] = $a;
    $bArr[] = $b;
    $xyArr[] = [$a, $b];
}

sort($aArr);
sort($bArr);
$aArr = array_values(array_unique($aArr));
$bArr = array_values(array_unique($bArr));

$aMap = array();
$bMap = array();

foreach ($aArr as $i => $v) {
    $aMap += array($v => $i+1);
}

foreach ($bArr as $i => $v) {
    $bMap += array($v => $i+1);
}

foreach ($xyArr as $v) {
    [$a, $b] = $v;
    printf("%d %d\n", $aMap[$a], $bMap[$b]);
}