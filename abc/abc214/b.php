<?php
fscanf(STDIN, "%d %d", $s, $t);
$c = 0;
for ($i = 0; $i <= 100; $i++) {
    for ($j = 0; $j <= 100; $j++) {
        for($k = 0; $k <= 100; $k++) {
            if ($i+$j+$k <= $s && $i*$j*$k <= $t) {
                $c++;
            }
        }
    }
}

echo $c;