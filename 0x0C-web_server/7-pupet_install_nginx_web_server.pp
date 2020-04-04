# install and configure an ubuntu servr 16.04 using puppet

package { 'nginx':
  ensure => installed,
  name   => 'nginx',
}

file { '/var/www/html/index.html':
  content => 'Holberton School for the win!',
  path    => '/var/www/html/index.html'
}

file_line { 'title':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  multiple => true
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
