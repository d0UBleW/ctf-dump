# Run script up to `function v3` in windows environment
# Get the final key value for each function v1, v2, v3

$key1 = "M0FBMUU3M0NFNEREQTkwOTY1REE1QjczNTM2NzQ1RjhEQzQwMTdFRkFBREVCRjRDODhERTQ4NDk3MDdFNDExRA=="

Set-Variable -Name CODE -Value (@(-7, -39, -16, 18, -12, 0, 7, -34, -5, -62, -38, -11, 1, -3, -17, -53, -18, -19, 46, 58))

$v1 = ""

foreach(${I} in (0 .. (${key1}.length-1))) {
    $v1 += [char]([int]([char]${key1}[${i}]) - ${Code}[${i}])
}

$v1



$key2 = "ODE5MDc5OTJERDQ4MzBDOTYyMDM3MDk4OTlGRDE4NTRFOThGQjYwQUZEMkVGQUE1OERGNzI1ODMyMDdBRTUzRA=="

Set-Variable -Name COde -Value (@(-6, 20, -35, -17, -7, -1, -21, -49, 6, 1, -8, -33, -18, -3, -23, -56, -11, 3, 5, 7))

$v2 = ""

foreach(${I} in (0 .. (${key2}.length-1))) {
    $v2 += [char]([system.int32]([char]${key2}[${i}]) - ${Code}[${i}])
}

$v2



$key3 = "Njg0ODg4QzBFQkIxN0YzNzQyOThCNjVFRTI4MDc1MjZDMDY2MDk0QzcwMUJDQzdFQkJFMUMxMDk1RjQ5NEZDMQ=="

Set-Variable -Name cODe -Value (@(-20, 35, -5, 0, -11, -20, 29, -52, -17, 52, 9, 3, 4, -15, -13, 35, -24, -33, 28, 61))

$v3 = ""

foreach(${I} in (0 .. (${key3}.length-1))) {
    $v3 += [char]([system.int32]([char]${key3}[${i}]) - ${Code}[${i}])
}

$v3
