# This manifest kills a process named killmenow
exec { 'pkill':
    command => 'pkil -f killmenow',
    path    => 'usr/bin',
}
