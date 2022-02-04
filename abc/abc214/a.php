<?php
fscanf(STDIN, "%d", $n);

if ($n <= 125) {
    echo 4;
} elseif ($n <= 211) {
    echo 6;
} else {
    echo 8;
}