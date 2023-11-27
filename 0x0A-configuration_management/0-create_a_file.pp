# This manifest creates a file at /tmp
file { 'Create_file':
    ensure  => 'file',
    path    => '/tmp/school'
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
   }