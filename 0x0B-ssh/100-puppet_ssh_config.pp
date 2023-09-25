# Client configuration file
include stdlib
file_line { 'NO password':
    ensure             => present,
    path               => '/etc/ssh/ssh_config',
    line               => '    PasswordAuthentication no',
    match              => '^PasswordAuthentication',
    append_on_no_match => true,
  }

file_line { 'New private key holder':
    ensure             => present,
    path               => '/etc/ssh/ssh_config',
    line               => '    IdentityFile ~/.ssh/school',
    match              => '^IdentityFile',
    append_on_no_match => true,
  }
