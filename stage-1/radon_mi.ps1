cd C:\ProgramData\Anaconda3\Lib\site-packages
function get_mi{
Param($p1,$p2)
radon mi $p1 -j -O $p2
}
get_mi -p1 $args[0] -p2 $args[1]