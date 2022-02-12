<?php
//error_reporting(E_ERROR);
fscanf(STDIN, "%s %d", $s, $k);

$array = getDict($s, $k);

printf("%s\n", $array[$k-1]);

function getDict($array_str, $k): array {
    $flags = array_fill(0, strlen($array_str), false);

    $array = recurt($array_str, $k, $flags, "");
    $array = array_unique($array);
    sort($array);
    return $array;
}

function recurt($array_str, $k, $flags, $s): array {
    $array = [];
    foreach(str_split($array_str) as $i => $v) {
        if ($flags[$i]) {
            continue;
        }

        $flags_temp = $flags;
        $flags_temp[$i] = true;
        $part = recurt($array_str, $k-1, $flags_temp, $s.$v);
        foreach($part as $w) {
            $array[] = $w;
        }
    }   

    return count($array) > 0 ? $array : [$s];
}