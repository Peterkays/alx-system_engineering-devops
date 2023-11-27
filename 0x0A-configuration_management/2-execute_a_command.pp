# This manifest kills a process named killmenow
exec { 'pkil':
    command => 'pkil -f killmenow',
    path    => 'usr/bin',
}