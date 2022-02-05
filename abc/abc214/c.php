<?php
error_reporting(E_ERROR);
fscanf(STDIN, "%d", $n);
$s = array_map("intval", explode(" ", fgets(STDIN)));
$t = array_map("intval", explode(" ", fgets(STDIN)));

$pq = new SplPriorityQueue();
foreach ($t as $i => $v) {
    $pq->insert(array($i, -$v), -$v);
}

$c = 0;
$ans = array_fill(0, $n, -1);
while (!$pq->isEmpty()) {
    [$i, $v] = $pq->extract();
    if ($ans[$i] == -1) {
        $c++;
        $ans[$i] = -$v;
        $pq->insert(array(($i+1)%$n,  $v-$s[$i]), $v-$s[$i]);
    }

    if ($c == $n) {
        break;
    }
}

foreach ($ans as $v) {
    printf("%d\n", $v);
}